# Power Automate flow for the assessment invitations

`scripts/send_invitations.py` decides what to send; the flow only creates,
updates or deletes the Outlook event. This recipe uses **standard connectors
only**, because the built-in *Request* connector (the `When an HTTP request is
received` trigger and the `Response` action) is premium and the M365 seeded
Power Automate does not include premium connectors.

The transport is therefore manual but batched:

```
script --batch  ──►  registrations/batch.json  ──►  paste into the flow
                                                        │
                                        emails the result (uid → event id)
                                                        ▼
script --import-results -  ◄──  copy the e-mail body  ◄─┘
```

Two manual steps per batch (~20–25 invitations twice a year). Everything else
— who to invite, waiting for the delegate and the room, changes, cancellations
— stays in the versioned script.

## Build the flow

1. <https://make.powerautomate.com> → **Create** → **Instant cloud flow** →
   trigger **Manually trigger a flow** (*Desencadenar manualmente un flujo*).
   Name it e.g. `GEO2022 assessment invitations`.
2. On the trigger, **Add an input** → **Text** → call it `payload`.
3. Add **Parse JSON** (*Analizar JSON*, a *Data Operation*):
   - **Content**: the `payload` token from the trigger.
   - **Schema**: paste this array schema (the batch is an array):

   ```json
   {
     "type": "array",
     "items": {
       "type": "object",
       "properties": {
         "action": {"type": "string"},
         "uid": {"type": "string"},
         "sequence": {"type": "integer"},
         "test": {"type": "boolean"},
         "form": {"type": "string"},
         "student": {"type": "string"},
         "subject": {"type": "string"},
         "start": {"type": "string"},
         "end": {"type": "string"},
         "timezone": {"type": "string"},
         "location": {"type": "string"},
         "body": {"type": "string"},
         "attendees": {"type": "array", "items": {"type": "string"}},
         "event_id": {"type": "string"}
       }
     }
   }
   ```

4. Add **Initialize variable** (*Inicializar variable*): name `Results`,
   type **Array**, no value. It must come before the loop.
5. Add **Apply to each** (*Aplicar a cada uno*), input = the **Body** output of
   *Parse JSON*. Inside it, add a **Switch** (*Modificador*) on the current
   item's `action`:

   ```
   items('Apply_to_each')?['action']
   ```

   (Spanish loop name: `items('Aplicar_a_cada_uno')?['action']`; use the
   dynamic-content picker and it writes the right reference for you.)

6. Set the three cases to `create`, `update` and `cancel`, and give each one
   its Outlook action plus an **Append to array variable** (*Anexar a la
   variable de matriz*, name `Results`):

   | case | action (fields from the current item) | appended value |
   |---|---|---|
   | `create` | **Create event (V4)** — Subject `subject` · Start `start` · End `end` · Time zone `timezone` · Required attendees `join(items('Apply_to_each')?['attendees'], ';')` · Location `location` · Body `body` · Show as Busy | `{"uid": "<uid>", "action": "create", "eventId": "<body/id of Create event>", "webLink": "<body/webLink>"}` |
   | `update` | **Update event (V4)** — Event id `event_id`, plus the same fields as `create` | `{"uid": "<uid>", "action": "update", "eventId": "<body/id of Update event>", "webLink": "<body/webLink>"}` |
   | `cancel` | **Delete event (V4)** — Event id `event_id` | `{"uid": "<uid>", "action": "cancel", "eventId": "<event_id>"}` |

   The id and link come from the connector's event object; in an expression
   that is `outputs('Create_event_(V4)')?['body/id']` and
   `outputs('Create_event_(V4)')?['body/webLink']` (the action name follows
   the display name: spaces become underscores, parentheses stay —
   `Crear_evento_(V4)` in Spanish). Insert them from **Dynamic content** when
   the designer offers them.

7. After the loop, add **Send an email (V2)** to yourself:
   - Subject: `GEO2022 invitation results`
   - Body: `@{string(variables('Results'))}` — the e-mail body *is* the JSON
     result array the script imports. Turn HTML off so nothing is mangled.

8. Save. Then per batch:

   ```sh
   python3 scripts/send_invitations.py --batch        # writes the batch
   # Power Automate → Run flow → paste registrations/batch.json into `payload`
   # copy the body of the results e-mail, then:
   pbpaste | python3 scripts/send_invitations.py --import-results -
   ```

   The batch is `registrations/batch.json`, or `batch_test.json` with `--test`
   (same for the state and pending files). Import the results **before**
   exporting the next batch, and do not run the flow twice for the same batch:
   the script only learns the event ids when the results are imported.

## Verifying

- `registrations/invitations_state.json` should gain an `event_id` per
  meeting. That id is what turns a later change (delegate appointed, room
  moved) into an **Update event** instead of a second meeting.
- `registrations/invitations_report.md` lists what was ready, waiting and
  blocked, and the batch that was written.
- If an id is missing from the results, the script says so; the next change
  would then create a new meeting, so check the run history and the calendar.

## Caveats worth knowing

- **Every create mails the attendees**, so test with `--test` first; it uses a
  dummy student and only the addresses in `registrations/invite_config.yml`
  (`test_to`), with its own state and batch files.
- **A failed run stops at the failure**: events created by earlier iterations
  exist but are not in the state until the results are imported. If a run
  fails, look at the calendar and the run history, delete anything stray, and
  export the batch again.
- **The trigger accepts the batch as text**, so keep an eye on the size when
  pasting (~20 invitations is a few tens of KB, fine).
- **Organizer** is whoever authorised the Outlook connection; the connector
  cannot create events in a shared mailbox.
- **DLP** can also block this flow if a tenant policy forbids combining
  connectors; all connectors here are standard, so it is much less likely than
  with the HTTP trigger.

## Later: the HTTP-trigger variant

If a Power Automate Premium licence ever appears, `--send` posts the same
payloads to a flow with the premium `When an HTTP request is received` trigger
and a `Response` action inside each case (event id from `body/id`), removing
the two manual steps. The script, the state file and every rule stay identical;
only the transport changes. See the git history of this file for that recipe.
