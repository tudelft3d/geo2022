(function () {
  "use strict";

  // One grade per category, half-points allowed (see the notes in the
  // "Rubric - Total" sheet of the rubric workbook). "< 5.75" counts as a 5
  // in the final-grade calculation.
  var grades = [
    { key: "lt575", label: "< 5.75", value: 5 },
    { key: "575", label: "5.75", value: 5.75 },
    { key: "6", label: "6", value: 6 },
    { key: "65", label: "6.5", value: 6.5 },
    { key: "7", label: "7", value: 7 },
    { key: "75", label: "7.5", value: 7.5 },
    { key: "8", label: "8", value: 8 },
    { key: "85", label: "8.5", value: 8.5 },
    { key: "9", label: "9", value: 9 },
    { key: "95", label: "9.5", value: 9.5 },
    { key: "10", label: "10", value: 10 },
  ];

  // Descriptors exist only at whole grades; half-points are judged between
  // the two neighbouring descriptors, so the table shows whole grades only.
  var descGrades = grades.filter(function (g) {
    return ["lt575", "6", "7", "8", "9", "10"].indexOf(g.key) !== -1;
  });

  var rubric = [    {
      id: "research",
      title: "Research",
      weight: 0.5,
      weightLabel: "50%",
      criteria: [
        {
          name: "Motivation",
          desc: {
            lt575:
              "No motivation is given, or the stated motivation does not match the work.",
            6: "Motivation can be broadly discerned, but is not well understood.",
            7: "Motivation can be understood and related to the problem.",
            8: "Motivation is clearly stated and explicitly connected to the specific research problem.",
            9: "Motivation is clearly argued and connected to the wider need for solutions of the problem.",
            10: "Motivation is argued convincingly, grounding the research in its wider scientific and practical context and making clear why the problem matters.",
          },
        },
        {
          name: "General problem",
          desc: {
            lt575:
              "The general problem cannot be explained; no specific research questions or objectives are given.",
            6: "The general problem is recognizable, but its scope and boundaries are not fully clear.",
            7: "The general problem is clear with defined boundaries (scope).",
            8: "The general problem is clear and has defined limitations.",
            9: "The general problem is clear, has boundaries or limitations and is feasible.",
            10: "The general problem is clear, has boundaries or limitations and is feasible with the approach proposed.",
          },
        },
        {
          name: "Theoretical framework",
          desc: {
            lt575: "No relevant theory is reproduced or applied to the research.",
            6: "Understands directly relevant theory at MSc level, but has difficulties applying it to the research.",
            7: "Understands directly relevant theory and applies it to the research after being shown how.",
            8: "Understands and can reproduce directly relevant theory at the level of MSc textbooks and scientific literature, and applies it to the research.",
            9: "Independently collects, processes and integrates theory from different fields or sources, and applies it to the research.",
            10: "Independently integrates and extends theory from different fields or sources, making a clear conceptual contribution to the research.",
          },
        },
        {
          name: "Literature / related work",
          desc: {
            lt575:
              "Unable to place the research in a wider context; no clear literature research; sources are accepted without reflection.",
            6: "Sufficient introduction and justification of the topic, but superficial (limited literature review).",
            7: "Sufficient introduction and justification of the topic, with fair literature support (decent literature review).",
            8: "Good introduction and justification of the topic with supporting literature (but not all included).",
            9: "Good introduction and justification of the topic, with vast literature support and critical evaluation of sources.",
            10: "Excellent introduction and justification of the topic, with all literature support, including recent related work by other researchers.",
          },
        },
        {
          name: "Choices of methods / data",
          desc: {
            lt575:
              "No adequate justification is given for the chosen methods and data, which are inappropriate for the research question.",
            6: "Choices of methods and data are partly justified, or their suitability for the research question is only weakly explained.",
            7: "Choices of methods and data are adequately justified and appropriate for the research question at hand.",
            8: "Choices of methods and data are justified, appropriate and logical, with only minor gaps in reasoning.",
            9: "Choices of methods and data are justified, logical and well-matched to the research question, with alternative approaches considered.",
            10: "The choices of methods and data are justified, logical and the most efficient at the moment.",
          },
        },
        {
          name: "Results / conclusions",
          desc: {
            lt575: "No substantial conclusions; results are left uninterpreted.",
            6: "Results are interpreted to a limited extent.",
            7: "Results are interpreted independently with a critical attitude.",
            8: "Results are interpreted critically and reflected upon within the broader scope of the discipline and its application.",
            9: "Beyond a critical, discipline-wide interpretation, the work proposes solutions or alternative approaches where the evidence is weak, showing how the results inform practice.",
            10: "The work offers a critical, discipline-wide reflection on the results and puts forward well-argued solutions or alternatives with clearly stated implications for future research and application.",
          },
        },
        {
          name: "Answers to research questions",
          desc: {
            lt575: "The results do not answer the research questions.",
            6: "The answers to the research questions are only partial or indirect; one or more questions are left unaddressed or answered tentatively.",
            7: "Each research question is addressed at a basic level, with limited depth or supporting evidence.",
            8: "The research questions are answered clearly and with supporting evidence, though minor gaps remain for one or two questions.",
            9: "The research questions are answered thoroughly and with strong evidence, with claims well supported across all questions.",
            10: "The research questions are answered comprehensively and convincingly, leaving no significant gaps and linking the answers back to the stated motivation.",
          },
        },
        {
          name: "Depth & ambition of the investigation",
          desc: {
            lt575:
              "The topic avoids meaningful challenge and the treatment is superficial; little genuine investigation is attempted.",
            6: "The topic is modest in scope and the treatment is largely surface-level, with limited independent investigation.",
            7: "The topic is appropriate for an MSc and is investigated to a satisfactory depth; the student engages the core problem without much extension.",
            8: "A moderately challenging topic taken to good depth, or a simpler topic explored thoroughly; the investigation goes beyond the obvious.",
            9: "A challenging topic investigated deeply, or a simpler topic taken to notable depth with rigorous analysis; clearly beyond minimum requirements.",
            10: "A demanding topic pursued with exceptional depth, or an apparently simple topic transformed through rigorous, thorough investigation; the level of inquiry is exemplary.",
          },
        },
      ],
    },
    {
      id: "process",
      title: "Process",
      weight: 0.2,
      weightLabel: "20%",
      criteria: [
        {
          name: "Autonomy / proactiveness",
          desc: {
            lt575:
              "Not autonomous or proactive at all; constant steering by supervisors is required.",
            6: "Sometimes autonomous and proactive, but generally needs steering by supervisors.",
            7: "Mostly autonomous; generally tries approaches before asking for help.",
            8: "Mostly autonomous and proactive, taking control of the project and steering it to completion with some hiccups.",
            9: "Autonomous and proactive, taking control of the project and steering it.",
            10: "Highly autonomous and proactive throughout, taking full control of the project and steering it efficiently.",
          },
        },
        {
          name: "Response to feedback / meetings with supervisors",
          desc: {
            lt575:
              "Does not respond to feedback or suggested alternatives; required changes are not implemented.",
            6: "Responds to feedback only minimally; implements few changes and shows little improvement.",
            7: "Contributes to discussions during meetings; critical attitude, but most key issues had to be pointed out by supervisors; uses feedback.",
            8: "Contributes to lively discussions; critical attitude, but key issues had to be pointed out; uses feedback for self-improvement.",
            9: "Leads lively discussions; critical attitude, pointing out the issues themselves; uses feedback for self-improvement.",
            10: "Leads lively discussions; critical own attitude; actively uses both own discoveries and feedback for self-improvement.",
          },
        },
        {
          name: "Use of resources",
          desc: {
            lt575: "Misuse of resources (data, computational time, people time).",
            6: "Makes inefficient but passable use of resources (e.g. tools, data, own/supervisor's time).",
            7: "Use of resources is appropriate (e.g. tools, data, own/supervisor's time).",
            8: "Makes good use of resources (e.g. tools, data, own/supervisor's time).",
            9: "Makes very good use of resources (e.g. tools, data, own/supervisor's time).",
            10: "Makes highly efficient use of resources (e.g. tools, data, own/supervisor's time).",
          },
        },
        {
          name: "Originality / creativity",
          desc: {
            lt575:
              "No original ideas within the project; most of the work is copied or already developed.",
            6: "Contribution to the project is somewhat original; limited initiative and suggestions within the project.",
            7: "Contribution to the project is partly original; some initiative and suggestions by the student.",
            8: "Contribution to the project is original, with suggestions by supervisors; several initiatives within the project.",
            9: "Contribution to the project is original, with almost no intervention by supervisors; many initiatives within the project.",
            10: "Contribution to the project is original; always takes initiative and makes suggestions within the project.",
          },
        },
        {
          name: "Planning",
          desc: {
            lt575: "No real planning; missed most of the deadlines.",
            6: "Basic timeline and plan prepared, but little followed or updated.",
            7: "Good timeline and plan prepared, often followed or updated.",
            8: "Prepared a good and feasible plan, mostly followed or adjusted when needed (e.g. according to progress and new findings).",
            9: "Prepared a clear and feasible plan, consistently followed and actively improved in response to progress and new findings.",
            10: "Prepared an efficient, clear and feasible plan, consistently followed and improved, managing changes smoothly and keeping the project on schedule.",
          },
        },
      ],
    },
    {
      id: "report",
      title: "Communication — Report",
      weight: 0.18,
      weightLabel: "18%",
      criteria: [
        {
          name: "Structure",
          desc: {
            lt575: "Report has no clear structure or logical flow.",
            6: "Report follows a structure, but with significant issues in clarity and organization.",
            7: "Report follows a structure, with some issues in clarity or organization that do not seriously impede understanding.",
            8: "Report follows a clear structure, with only minor issues in clarity.",
            9: "Report follows a clear and logical structure throughout.",
            10: "Report follows a clear and logical structure in which every section serves the argument and guides the reader.",
          },
        },
        {
          name: "Documentation of work done",
          desc: {
            lt575:
              "The report omits key parts of the research, so the process and results cannot be understood.",
            6: "The report documents the research only partially; important steps are missing or unclear.",
            7: "The report documents all main parts of the research, so the process can be followed.",
            8: "The report documents all parts of the research clearly, including data handling and key decisions.",
            9: "The report documents all parts of the research in detail, including data handling, decisions and assumptions.",
            10: "The report documents every part of the research in detail, giving a complete and faithful account of the process.",
          },
        },
        {
          name: "Writing",
          desc: {
            lt575: "Writing is disorganized, with pervasive errors that obscure meaning.",
            6: "Report is written with limited clarity and contains significant errors that need correction.",
            7: "Report is generally well written, but contains a number of errors and needs improvements.",
            8: "Report is generally well written, but contains a few errors and needs improvements.",
            9: "Report is well written, with very few writing errors.",
            10: "Report is well written using clear scientific language, with few errors.",
          },
        },
        {
          name: "Abstract",
          desc: {
            lt575: "Abstract is missing or fails to summarize the work.",
            6: "Abstract captures little of the work, or is unbalanced in what it covers.",
            7: "Abstract captures the main elements of the work, with some gaps in coverage.",
            8: "Abstract captures most of the work, including the main methods and results.",
            9: "Abstract captures the essence of the work, covering aim, method and main results.",
            10: "Abstract captures the essence of the work in a concise and complete summary.",
          },
        },
        {
          name: "Use of references",
          desc: {
            lt575: "Sources are not acknowledged; references are missing or unreliable.",
            6: "Other work is acknowledged to a limited extent; the reference list is incomplete or inconsistent.",
            7: "Report properly acknowledges other work broadly and contains a fair list of references.",
            8: "Report properly acknowledges other work most of the time, with a mostly complete reference list.",
            9: "Report properly acknowledges other work consistently, with a complete reference list and only minor formatting issues.",
            10: "Report properly acknowledges other work everywhere and contains a complete and well-formatted reference list.",
          },
        },
        {
          name: "Supplementary output / data",
          desc: {
            lt575: "No supplementary output or data is provided.",
            6: "Supplementary output or data is mentioned, but is broken, incomplete or unusable.",
            7: "Work yields limited but usable supplementary output (e.g. software, data).",
            8: "Work yields useful supplementary output (e.g. software, data), which is added to the report.",
            9: "Work yields substantial supplementary output, which is added to the report and made available to the reader.",
            10: "Work yields substantial, well-documented supplementary output (e.g. software, data), which is made publicly available alongside the report.",
          },
        },
        {
          name: "Reproducibility / open science",
          desc: {
            lt575: "The research process cannot be reproduced or verified.",
            6: "Reproducibility is poor; code, data or parameters are missing or undocumented.",
            7: "The research is mostly reproducible; code and data are documented at a basic level.",
            8: "The research is reproducible; code and data are organized and documented.",
            9: "The research is reproducible following good open science practices (e.g. version control, documentation).",
            10: "The research is fully reproducible by others: code, data and parameters are complete, documented and publicly available following open science best practices.",
          },
        },
      ],
    },
    {
      id: "pres",
      title: "Communication — Presentation",
      weight: 0.12,
      weightLabel: "12%",
      criteria: [
        {
          name: "Structure",
          desc: {
            lt575: "Presentation is chaotic; structure not clear.",
            6: "Presentation follows a structure, but with significant issues in clarity and organization.",
            7: "Presentation follows a structure, with some issues in clarity or organization.",
            8: "Presentation follows a clear structure, with only minor issues.",
            9: "Presentation follows a clear structure with good pacing and transitions.",
            10: "Presentation follows a clear, logical and well-paced structure that leads the audience through the argument.",
          },
        },
        {
          name: "Content",
          desc: {
            lt575:
              "Presentation does not convey the motivation, problem or main results of the work.",
            6: "Presentation gives a partial summary of the work; some key points are missing or unclear.",
            7: "Presentation gives a decent summary of motivation, problem, work done, results and conclusions.",
            8: "Presentation gives a good summary of motivation, problem, work done, results and conclusions.",
            9: "Presentation gives a very good summary of motivation, problem, work done, results and conclusions.",
            10: "Presentation gives a concise, complete and easy-to-follow summary of motivation, problem, work done, results and conclusions.",
          },
        },
        {
          name: "Visual material",
          desc: {
            lt575: "Visual material is missing or of poor quality.",
            6: "Basic presentation material (e.g. slides, videos, demos), functional but plain.",
            7: "Adequate presentation material that supports the talk.",
            8: "Good presentation material, with clean visuals that support the talk.",
            9: "Very good presentation material, with well-designed visuals.",
            10: "Excellent presentation material, with clear, well-designed visuals that strengthen the talk.",
          },
        },
        {
          name: "Audience / attention",
          desc: {
            lt575: "Loses the audience rapidly.",
            6: "Interaction with the audience is sufficient (eye contact, body language, tone of voice, pace of speaking); gets the attention of the audience.",
            7: "Interaction with the audience is appropriate; gets the attention of the audience and maintains it to some extent.",
            8: "Interaction with the audience is good; maintains the attention of the audience for most of the presentation.",
            9: "Interaction with the audience is very good; maintains constant attention of the audience.",
            10: "Interaction with the audience is excellent; maintains constant attention of the audience throughout.",
          },
        },
        {
          name: "Responses to questions",
          desc: {
            lt575: "Candidate cannot address the questions posed.",
            6: "Candidate answers some questions correctly, but answers are superficial or incomplete.",
            7: "Candidate answers most questions correctly, with a few gaps.",
            8: "Candidate answers questions correctly, with a clear explanation of the reasoning.",
            9: "Candidate answers questions correctly and responds well to follow-up questions.",
            10: "Questions are answered succinctly and with full awareness of the strengths and weaknesses of the research.",
          },
        },
        {
          name: "Understanding",
          desc: {
            lt575:
              "Demonstrates a clear lack of understanding of the scientific problem and cannot explain the work.",
            6: "Shows superficial knowledge of the topic; struggles when probed beyond the slides.",
            7: "Explains the work competently for its intended application; handles the main questions but shows occasional gaps when probed on details.",
            8: "Explains the work confidently at a research-and-development level; handles most probing questions without hesitation.",
            9: "Masters the content of the research topic; answers probing questions fluently and can articulate the work's limitations.",
            10: "Masters the content well beyond the immediate research topic; situates the work in the wider field and discusses limitations and implications unprompted.",
          },
        },
      ],
    },
  ];

  var notes = [
    "Enter one grade per category (half-points allowed).",
    "Descriptors exist at whole grades; half-points are judged between the two neighbouring descriptors.",
    "Pass threshold: 5.75. Grades of 5.75 and higher round up to 6 and count as a pass.",
    "No sub-weights per aspect: aspects are a checklist to support judgment. Assessors look at where most elements fall within a category and decide one grade per category.",
    "\u201CDepth & ambition of the investigation\u201D (Research): bands reward the level of genuine inquiry delivered. A demanding topic taken to good depth, or a simpler topic taken to exceptional depth, both reach the top bands.",
  ];

  function esc(s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
  }

  function gradeValue(key) {
    for (var i = 0; i < grades.length; i++) {
      if (grades[i].key === key) return grades[i].value;
    }
    return null;
  }

  // Per-aspect marks are working notes for the assessors: the resulting
  // average is advisory only and never enters the summary, final grade or
  // PDF — those use the explicitly chosen category grade.
  var aspectMarks = {};

  function buildRefTable(section) {
    return (
      '<table class="ref-table"><thead><tr><th>Aspect</th>' +
      descGrades
        .map(function (g) {
          return "<th>" + esc(g.label) + "</th>";
        })
        .join("") +
      "</tr></thead><tbody>" +
      section.criteria
        .map(function (c, ci) {
          return (
            "<tr><td>" +
            esc(c.name) +
            "</td>" +
            descGrades
              .map(function (g) {
                return (
                  '<td class="sel-cell" data-section="' +
                  section.id +
                  '" data-aspect="' +
                  ci +
                  '" data-grade="' +
                  g.key +
                  '">' +
                  esc(c.desc[g.key] || "—") +
                  "</td>"
                );
              })
              .join("") +
            "</tr>"
          );
        })
        .join("") +
      "</tbody></table>"
    );
  }

  function buildRubric() {
    var container = document.getElementById("rubricContainer");
    if (!container) return;
    rubric.forEach(function (section) {
      aspectMarks[section.id] = section.criteria.map(function () {
        return null;
      });
      var sec = document.createElement("div");
      sec.className = "section";
      sec.innerHTML =
        '<div class="section-header">' +
        "<span>" +
        esc(section.title) +
        "</span>" +
        '<span class="weight">' +
        section.weightLabel +
        "</span>" +
        "</div>" +
        '<div class="section-body">' +
        '<div style="overflow-x:auto">' +
        buildRefTable(section) +
        "</div>" +
        '<div class="grade-row"><span class="grade-row-label">Grade for this category</span>' +
        grades
          .map(function (g) {
            var id = "grade_" + section.id + "_" + g.key;
            return (
              '<span class="grade-option"><input type="radio" name="grade_' +
              section.id +
              '" value="' +
              g.value +
              '" data-label="' +
              esc(g.label) +
              '" id="' +
              id +
              '" onchange="updateSummary()"><label for="' +
              id +
              '">' +
              esc(g.label) +
              "</label></span>"
            );
          })
          .join("") +
        '<span class="advisory" id="advisory_' +
        section.id +
        '"></span>' +
        "</div>" +
        '<div class="comments-block"><label for="comments_' +
        section.id +
        '">Comments for ' +
        esc(section.title.toLowerCase()) +
        '</label><textarea id="comments_' +
        section.id +
        '" placeholder="Comments…"></textarea></div>' +
        "</div>";
      container.appendChild(sec);
      updateAdvisory(section.id);
    });

    container.addEventListener("click", function (e) {
      var td = e.target.closest("td.sel-cell");
      if (!td) return;
      var sectionId = td.getAttribute("data-section");
      var aspect = parseInt(td.getAttribute("data-aspect"), 10);
      var grade = td.getAttribute("data-grade");
      var marks = aspectMarks[sectionId];
      if (!marks) return;
      // Clicking the selected descriptor again clears the aspect's mark.
      marks[aspect] = marks[aspect] === grade ? null : grade;
      Array.prototype.forEach.call(
        td.parentNode.querySelectorAll("td.sel-cell"),
        function (c) {
          c.classList.remove("selected");
        },
      );
      if (marks[aspect] !== null) td.classList.add("selected");
      updateAdvisory(sectionId);
    });

    var notesEl = document.getElementById("rubricNotes");
    if (notesEl) {
      notesEl.innerHTML =
        "<h2>Notes</h2><ul>" +
        notes
          .map(function (n) {
            return "<li>" + esc(n) + "</li>";
          })
          .join("") +
        "</ul>";
    }
  }

  function updateAdvisory(sectionId) {
    var el = document.getElementById("advisory_" + sectionId);
    if (!el) return;
    var marks = aspectMarks[sectionId] || [];
    var values = [];
    marks.forEach(function (key) {
      if (key !== null) values.push(gradeValue(key));
    });
    if (!values.length) {
      el.innerHTML = "Advisory average: —";
      return;
    }
    var avg =
      values.reduce(function (a, b) {
        return a + b;
      }, 0) / values.length;
    el.innerHTML =
      "Advisory average: <strong>" +
      avg.toFixed(1) +
      '</strong> <span class="advisory-count">(' +
      values.length +
      " of " +
      marks.length +
      " aspects marked)</span>";
  }

  function getSelectedGrades() {
    var results = {};
    rubric.forEach(function (section) {
      var sel = document.querySelector(
        'input[name="grade_' + section.id + '"]:checked',
      );
      results[section.id] = sel
        ? { value: parseFloat(sel.value), label: sel.getAttribute("data-label") }
        : null;
    });
    return results;
  }

  function getCommAvg(r) {
    if (r.report && r.pres) {
      return r.report.value * 0.6 + r.pres.value * 0.4;
    }
    if (r.report) return r.report.value;
    if (r.pres) return r.pres.value;
    return null;
  }

  function getFinal(r) {
    var commAvg = getCommAvg(r);
    if (r.research && r.process && commAvg !== null) {
      return r.research.value * 0.5 + r.process.value * 0.2 + commAvg * 0.3;
    }
    return null;
  }

  function updateSummary() {
    var r = getSelectedGrades();
    var setEl = function (id, val) {
      var el = document.getElementById(id);
      if (el) {
        el.textContent = val !== null ? val : "—";
      }
    };

    setEl(
      "sumResearchAvg",
      r.research ? r.research.label : null,
    );
    setEl("sumProcessAvg", r.process ? r.process.label : null);
    setEl("sumReportAvg", r.report ? r.report.label : null);
    setEl("sumPresAvg", r.pres ? r.pres.label : null);

    var final = getFinal(r);
    var finalEl = document.getElementById("sumFinal");
    if (finalEl) {
      if (final !== null) {
        var rounded = Math.round(final * 2) / 2;
        var pass = rounded >= 5.75;
        finalEl.innerHTML =
          rounded.toFixed(1) +
          " (" +
          final.toFixed(2) +
          ') <span class="verdict ' +
          (pass ? "pass" : "fail") +
          '">' +
          (pass ? "Pass" : "Fail") +
          "</span>";
      } else {
        finalEl.textContent = "—";
      }
    }
  }

  function resetAll() {
    document
      .querySelectorAll('input[type="radio"]')
      .forEach(function (r) {
        r.checked = false;
      });
    document
      .querySelectorAll("td.sel-cell.selected")
      .forEach(function (c) {
        c.classList.remove("selected");
      });
    Object.keys(aspectMarks).forEach(function (sectionId) {
      aspectMarks[sectionId] = aspectMarks[sectionId].map(function () {
        return null;
      });
      updateAdvisory(sectionId);
    });
    updateSummary();
  }

  var logoUrl = (function () {
    var el = document.querySelector(".rubric-page");
    return el && el.dataset.logo ? el.dataset.logo : "";
  })();
  var logoDataUrl = null;

  function loadLogo() {
    return new Promise(function (resolve) {
      if (!logoUrl) {
        resolve();
        return;
      }
      fetch(logoUrl)
        .then(function (r) {
          return r.text();
        })
        .then(function (svgText) {
          var blob = new Blob([svgText], { type: "image/svg+xml" });
          var url = URL.createObjectURL(blob);
          var img = new Image();
          img.onload = function () {
            var canvas = document.createElement("canvas");
            canvas.width = 425;
            canvas.height = 121;
            canvas.getContext("2d").drawImage(img, 0, 0, 425, 121);
            URL.revokeObjectURL(url);
            logoDataUrl = canvas.toDataURL("image/png");
            resolve();
          };
          img.onerror = function () {
            URL.revokeObjectURL(url);
            resolve();
          };
          img.src = url;
        })
        .catch(function () {
          resolve();
        });
    });
  }

  window.updateSummary = updateSummary;
  window.resetAll = resetAll;
  window.generatePDF = generatePDF;

  async function generatePDF() {
    try {
      var JsPDF = window.jspdf && (window.jspdf.jsPDF || window.jsPDF);
      if (!JsPDF) {
        alert("jsPDF library not loaded. Check internet connection.");
        return;
      }
      if (typeof window.applyPlugin === "function") {
        window.applyPlugin(JsPDF);
      }
      await loadLogo();
      var doc = new JsPDF("p", "mm", "a4");
      var pageW = doc.internal.pageSize.getWidth();
      var margin = 14;
      var y = 10;
      var lineH = 5;
      var gap = 4;

      var drawHeader = function () {
        doc.setFillColor(43, 84, 33);
        doc.rect(0, 0, pageW, 14, "F");
        doc.setTextColor(255, 255, 255);
        doc.setFont("helvetica", "bold");
        doc.setFontSize(10);
        doc.text(
          "MSc Geomatics — Thesis Assessment Rubric — TU Delft",
          margin,
          9,
        );
        if (logoDataUrl) {
          var lh = 8;
          var lw = lh * (425 / 121);
          doc.addImage(logoDataUrl, "PNG", pageW - margin - lw, (14 - lh) / 2, lw, lh);
        }
      };

      var newPage = function () {
        doc.addPage();
        drawHeader();
        y = 16;
      };

      var checkSpace = function (needed) {
        if (y + needed > 287) newPage();
      };

      var wrap = function (text, w, size) {
        doc.setFontSize(size);
        return doc.splitTextToSize(text, w);
      };

      drawHeader();
      y = 18;

      doc.setTextColor(0, 0, 0);
      doc.setFontSize(9);
      var sid = function (id) {
        var el = document.getElementById(id);
        return el ? el.value || "" : "";
      };
      var info = [
        ["Student:", sid("studentName")],
        ["Student nr:", sid("studentNumber")],
        ["Delegate of BoE:", sid("delegateBoE")],
        ["Supervisor:", sid("respSupervisor")],
        ["2nd supervisor:", sid("secondSupervisor")],
        ["Co-reader:", sid("coreader")],
        ["Thesis:", sid("thesisTitle")],
        ["Date:", sid("assessmentDate")],
      ];
      info.forEach(function (row) {
        doc.setFont("helvetica", "bold");
        doc.text(row[0], margin, y);
        doc.setFont("helvetica", "normal");
        doc.text(row[1] || "—", margin + 28, y);
        y += lineH;
      });
      y += gap;

      checkSpace(40);
      doc.setFont("helvetica", "bold");
      doc.setFontSize(11);
      doc.text("Grade Summary", margin, y);
      y += lineH;
      var r = getSelectedGrades();
      var final = getFinal(r);
      var fmt = function (sel) {
        return sel ? sel.label : "—";
      };
      var fmtFinal = function (v) {
        if (v === null) return "—";
        var rounded = Math.round(v * 2) / 2;
        return (
          rounded.toFixed(1) + " (" + v.toFixed(2) + ")" +
          (rounded >= 5.75 ? " — pass" : " — fail")
        );
      };
      var rows = [
        ["Research", "50%", fmt(r.research)],
        ["Process", "20%", fmt(r.process)],
        ["Communication — Report", "18%", fmt(r.report)],
        ["Communication — Presentation", "12%", fmt(r.pres)],
        ["Final Grade", "100%", fmtFinal(final)],
      ];
      doc.autoTable({
        startY: y,
        margin: { left: margin },
        head: [["Category", "Weight", "Grade"]],
        body: rows,
        styles: {
          fontSize: 9,
          cellPadding: 2,
          lineColor: [200, 212, 198],
          lineWidth: 0.1,
        },
        headStyles: {
          fillColor: [43, 84, 33],
          textColor: [255, 255, 255],
          fontStyle: "bold",
        },
        didParseCell: function (data) {
          if (data.row.index === rows.length - 1) {
            data.cell.styles.fontStyle = "bold";
          }
        },
        bodyStyles: { textColor: [0, 0, 0] },
        alternateRowStyles: { fillColor: [242, 246, 241] },
      });
      y = doc.lastAutoTable.finalY + gap;

      rubric.forEach(function (section) {
        checkSpace(30);
        var gradeLabel = r[section.id] ? r[section.id].label : "—";
        doc.setFillColor(43, 84, 33);
        doc.rect(margin, y, pageW - margin * 2, 6, "F");
        doc.setTextColor(255, 255, 255);
        doc.setFont("helvetica", "bold");
        doc.setFontSize(10);
        doc.text(
          section.title + " (" + section.weightLabel + ") — Grade: " + gradeLabel,
          margin + 2,
          y + 4.5,
        );
        y += 8;

        var commentsEl = document.getElementById("comments_" + section.id);
        var comments = commentsEl ? commentsEl.value || "" : "";
        doc.setTextColor(0, 0, 0);
        doc.setFont("helvetica", "italic");
        doc.setFontSize(9);
        doc.text("Comments:", margin, y);
        y += lineH;
        doc.setFont("helvetica", "normal");
        if (comments.trim()) {
          var lines = wrap(comments, pageW - margin * 2, 9);
          checkSpace(lines.length * lineH + 4);
          doc.text(lines, margin, y);
          y += lines.length * lineH;
        } else {
          doc.setTextColor(120, 120, 120);
          doc.text("(no comments)", margin, y);
          doc.setTextColor(0, 0, 0);
          y += lineH;
        }
        y += gap;
      });

      var generalEl = document.getElementById("generalComments");
      var general = generalEl ? generalEl.value || "" : "";
      checkSpace(20);
      doc.setFont("helvetica", "bold");
      doc.setFontSize(11);
      doc.text("Additional Comments / Feedback for the Student", margin, y);
      y += lineH + 1;
      doc.setFont("helvetica", "normal");
      doc.setFontSize(9);
      if (general.trim()) {
        var gLines = wrap(general, pageW - margin * 2, 9);
        checkSpace(gLines.length * lineH + 4);
        doc.text(gLines, margin, y);
        y += gLines.length * lineH;
      } else {
        doc.setTextColor(120, 120, 120);
        doc.text("(no comments)", margin, y);
        doc.setTextColor(0, 0, 0);
        y += lineH;
      }
      y += gap;

      checkSpace(20 + notes.length * lineH * 2);
      doc.setFont("helvetica", "bold");
      doc.setFontSize(11);
      doc.text("Notes", margin, y);
      y += lineH + 1;
      doc.setFont("helvetica", "normal");
      doc.setFontSize(9);
      notes.forEach(function (n) {
        var nLines = wrap("• " + n, pageW - margin * 2, 9);
        checkSpace(nLines.length * lineH);
        doc.text(nLines, margin, y);
        y += nLines.length * lineH;
      });

      doc.save("thesis-assessment.pdf");
    } catch (err) {
      alert("PDF generation error: " + err.message);
      console.error(err);
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    buildRubric();
    updateSummary();
  });
})();
