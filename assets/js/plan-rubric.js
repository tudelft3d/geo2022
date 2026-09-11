(function () {
  "use strict";

  var marks = [
    { key: "go", label: "Go" },
    { key: "borderline", label: "Borderline" },
    { key: "nogo", label: "No-go" },
  ];

  var aspects = [
    {
      name: "Motivation",
      go: "Motivation is clearly stated and explicitly connected to the specific research problem and the context of geomatics.",
      borderline:
        "Motivation can be broadly discerned, but is not clearly connected to the specific research problem.",
      nogo: "No motivation is given, or the stated motivation does not match the proposed work.",
    },
    {
      name: "Problem & research questions",
      go: "The problem statement is clear with defined boundaries (scope) and is feasible; research questions are clearly defined with an explicit scope of what will and will not be done.",
      borderline:
        "The problem or research questions are recognizable, but their scope or boundaries are not fully clear.",
      nogo: "The problem cannot be explained, or no specific research questions or objectives are given.",
    },
    {
      name: "Related work / literature",
      go: "Relevant literature is presented and linked to the project, with adequate justification of the topic.",
      borderline:
        "A sufficient introduction to the topic is given, but the literature review is limited or only weakly linked to the project.",
      nogo: "The research is not placed in a wider context; literature is missing or superficial, and sources are accepted without reflection.",
    },
    {
      name: "Methodology (methods / data)",
      go: "The proposed methods and data are adequately justified and appropriate for the research questions.",
      borderline:
        "Methods and data are partly justified, or their suitability for the research question is only weakly explained.",
      nogo: "No adequate justification is given for the chosen methods and data, which are inappropriate for the research question.",
    },
    {
      name: "Feasibility & time planning",
      go: "A realistic time plan (e.g. Gantt chart) is given; the project is feasible within the graduation period and key risks are identified.",
      borderline:
        "A time plan is given, but is optimistic or loosely linked to the work; risks are not clearly identified.",
      nogo: "No real time planning is given, or the plan is not feasible within the graduation period.",
    },
    {
      name: "Autonomy & use of supervision",
      go: "Mostly autonomous and proactive; responds to feedback and contributes to meetings; implements suggested changes.",
      borderline:
        "Sometimes autonomous, but generally needs steering; responds to feedback only minimally.",
      nogo: "Not autonomous or proactive; constant steering required; does not respond to feedback or implement changes.",
    },
    {
      name: "Structure & writing",
      go: "Plan follows a clear structure with the required elements (introduction, related work, research questions, methodology, time planning, data & tools, references) and is generally well written with few errors.",
      borderline:
        "Plan follows a structure but with some issues in clarity/organisation; writing has a number of errors needing correction.",
      nogo: "Plan has no clear structure or logical flow; writing is disorganized with pervasive errors that obscure meaning.",
    },
    {
      name: "References & AI disclosure",
      go: "Other work is acknowledged properly with a complete, consistent reference list; if AI/LLMs were used, a disclosure statement describes tools, use and extent.",
      borderline:
        "References are present but incomplete or inconsistent; or AI use is disclosed only partially.",
      nogo: "Sources are not acknowledged or references missing/unreliable; or AI/LLMs were used without the required disclosure statement.",
    },
    {
      name: "Content & structure",
      go: "Presentation follows a clear structure and gives a good summary of motivation, problem, research questions, methodology and planning.",
      borderline:
        "Presentation follows a structure but with minor issues; summary covers most key elements.",
      nogo: "Presentation is chaotic or does not convey the motivation, problem or main elements of the plan.",
    },
    {
      name: "Delivery & visual material",
      go: "Adequate presentation material supports the talk; interaction with the audience is appropriate and maintains attention.",
      borderline:
        "Basic but functional material; interaction with the audience is sufficient though not always maintained.",
      nogo: "Visual material is missing or of poor quality; loses the audience rapidly.",
    },
    {
      name: "Understanding & Q&A",
      go: "Candidate answers most questions correctly and is confident with the content for its application; understands the plan and its implications.",
      borderline:
        "Candidate answers some questions but with gaps or superficial reasoning when probed.",
      nogo: "Candidate cannot address the questions posed or demonstrates a clear lack of understanding of the problem.",
    },
  ];

  var notes = [
    "Mark each aspect Go / Borderline / No-go by clicking the description that best matches it.",
    "The pattern of marks is indicative. Supervisors review where aspects fall and make the final Go/No-go decision.",
    "A No-go on an essential aspect, or several Borderline/No-go marks, supports a No-go.",
    "Procedure: 15 min presentation, 15 min questions (second then responsible supervisor), 15 min deliberation and feedback. Quorum: both supervisors and the delegate.",
    "Deliverable: graduation plan uploaded to MyCase 1 week before the assessment (unless the responsible supervisor agrees otherwise).",
  ];

  function esc(s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
  }

  // Per-aspect marks: clicking a Go/Borderline/No-go descriptor cell marks
  // that aspect; clicking the selected cell again clears it.
  var aspectMarks = [];

  function buildPlan() {
    var container = document.getElementById("planContainer");
    if (!container) return;
    aspectMarks = aspects.map(function () {
      return null;
    });
    var sec = document.createElement("div");
    sec.className = "section";
    sec.innerHTML =
      '<div class="section-header">' +
      "<span>Aspects</span>" +
      '<span class="weight">Go / Borderline / No-go</span>' +
      "</div>" +
      '<div class="section-body">' +
      '<div style="overflow-x:auto">' +
      '<table class="marks-table"><thead><tr><th>Aspect</th><th>Go</th><th>Borderline</th><th>No-go</th></tr></thead><tbody>' +
      aspects
        .map(function (a, ai) {
          return (
            "<tr><td>" +
            esc(a.name) +
            "</td>" +
            marks
              .map(function (m) {
                return (
                  '<td class="sel-cell ' +
                  m.key +
                  '" data-aspect="' +
                  ai +
                  '" data-mark="' +
                  m.label +
                  '">' +
                  esc(a[m.key]) +
                  "</td>"
                );
              })
              .join("") +
            "</tr>"
          );
        })
        .join("") +
      "</tbody></table></div>" +
      "</div>";
    container.appendChild(sec);

    container.addEventListener("click", function (e) {
      var td = e.target.closest("td.sel-cell");
      if (!td) return;
      var aspect = parseInt(td.getAttribute("data-aspect"), 10);
      var mark = td.getAttribute("data-mark");
      aspectMarks[aspect] = aspectMarks[aspect] === mark ? null : mark;
      Array.prototype.forEach.call(
        td.parentNode.querySelectorAll("td.sel-cell"),
        function (c) {
          c.classList.remove("selected");
        },
      );
      if (aspectMarks[aspect] !== null) td.classList.add("selected");
      updateDecision();
    });

    var notesEl = document.getElementById("planNotes");
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

  function getDecision() {
    var counts = { Go: 0, Borderline: 0, "No-go": 0 };
    aspectMarks.forEach(function (m) {
      if (m) counts[m]++;
    });
    var finalEl = document.querySelector(
      'input[name="finalDecision"]:checked',
    );
    return { counts: counts, final: finalEl ? finalEl.value : null };
  }

  function updateDecision() {
    var d = getDecision();
    document.getElementById("sumGo").textContent = d.counts.Go;
    document.getElementById("sumBorderline").textContent = d.counts.Borderline;
    document.getElementById("sumNogo").textContent = d.counts["No-go"];
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
    aspectMarks = aspectMarks.map(function () {
      return null;
    });
    updateDecision();
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

  window.updateDecision = updateDecision;
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
          "MSc Geomatics — Kick-off (Thesis Plan) Assessment — TU Delft",
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

      checkSpace(50);
      var d = getDecision();
      doc.setFont("helvetica", "bold");
      doc.setFontSize(11);
      doc.text("Decision Summary", margin, y);
      y += lineH;
      var rows = [
        ["Aspects marked Go", String(d.counts.Go)],
        ["Aspects marked Borderline", String(d.counts.Borderline)],
        ["Aspects marked No-go", String(d.counts["No-go"])],
        ["Final decision (Go / No-go)", d.final || "—"],
      ];
      doc.autoTable({
        startY: y,
        margin: { left: margin },
        head: [["Outcome", "Result"]],
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

      checkSpace(40);
      doc.setFillColor(43, 84, 33);
      doc.rect(margin, y, pageW - margin * 2, 6, "F");
      doc.setTextColor(255, 255, 255);
      doc.setFont("helvetica", "bold");
      doc.setFontSize(10);
      doc.text("Aspects (Go / Borderline / No-go)", margin + 2, y + 4.5);
      y += 8;

      var aspectRows = aspects.map(function (a, ai) {
        return [a.name, aspectMarks[ai] || "—"];
      });
      doc.autoTable({
        startY: y,
        margin: { left: margin },
        head: [["Aspect", "Mark"]],
        body: aspectRows,
        styles: {
          fontSize: 8,
          cellPadding: 1.5,
          lineColor: [200, 212, 198],
          lineWidth: 0.1,
        },
        headStyles: {
          fillColor: [200, 212, 198],
          textColor: [43, 84, 33],
          fontStyle: "bold",
          fontSize: 8,
        },
        bodyStyles: { textColor: [0, 0, 0] },
        alternateRowStyles: { fillColor: [242, 246, 241] },
        columnStyles: {
          0: { cellWidth: pageW - margin * 2 - 28 },
          1: { cellWidth: 28, halign: "center" },
        },
      });
      y = doc.lastAutoTable.finalY + gap;

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

      doc.save("kick-off-assessment.pdf");
    } catch (err) {
      alert("PDF generation error: " + err.message);
      console.error(err);
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    buildPlan();
    updateDecision();
  });
})();
