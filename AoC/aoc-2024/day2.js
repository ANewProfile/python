import { readFile } from 'fs/promises';

const parse = (input) => {
    let trimmedInput = input.trimEnd();
    let reportsWithoutSplitLevels = trimmedInput.split("\n");
    let reportsSplitLevels = [];
    for (let i = 0; i < reportsWithoutSplitLevels.length; i++) {  // cycle through reports
        let splitLevel = reportsWithoutSplitLevels[i].split(" ");  // splits the report into levels
        let reportWithSplitLevels = [];   // full report at i
        for (let i = 0; i < splitLevel.length; i++) {
            reportWithSplitLevels.push(parseInt(splitLevel[i]));  // adds level to full report
        }
        reportsSplitLevels.push(reportWithSplitLevels);  // adds full report to reports
    }
    return reportsSplitLevels
}

const reportIsSafe = (report) => {
    var increasing;
    if (report[0] < report[1]) {
        increasing = true;
    } else {
        increasing = false;
    }

    for (let i = 1; i < report.length; i++) {
        if (Math.abs(report[i] - report[i - 1]) < 1) {  // if dist btwn nums is <1
            return false
        }
        if (Math.abs(report[i] - report[i - 1]) > 3) {  // if dist btwn nums is >3
            return false
        }

        if (report[i] > report[i - 1] && !increasing) {  // if nums are increasing but first is decreasing
            return false
        }

        if (report[i] < report[i - 1] && increasing) { //if nums are decreasing but first is increasing
            return false
        }
    }

    return true
}

const dampnerReportIsSafe = (report) => {
    var newReport;
    for (let i = 0; i < report.length; i++) {
        newReport = Array.from(report)
        let bad = false;

        var increasing;
        if (report[0] < report[1]) {
            increasing = true;
        } else {
            increasing = false;
        }

        if (newReport[0] < newReport[1]) {
            increasing = true;
        } else {
            increasing = false;
        }


        for (let j = 1; j < newReport.length; j++) {
            if (Math.abs(newReport[j] - newReport[j - 1]) < 1) {  // if dist btwn nums is <1
                bad = true;
                break
            }
            if (Math.abs(newReport[j] - newReport[j - 1]) > 3) {  // if dist btwn nums is >3
                bad = true;
                break
            }

            if (newReport[j] > newReport[j - 1] && !increasing) {  // if nums are increasing but first is decreasing
                bad = true;
                break
            }

            if (newReport[j] < newReport[j - 1] && increasing) { //if nums are decreasing but first is increasing
                bad = true;
                break
            }
        }

        if (bad) { continue; }
        else { return true; }
    }
}


let input = await readFile('/Users/littletheo/non-git/aoc-2024/day2input.txt', 'utf8');
let reports = parse(input);

// Find safe reports
let safeReports = 0;
for (let i = 0; i < reports.length; i++) {
    if (dampnerReportIsSafe(reports[i])) {
        safeReports++;
    }
}

console.log(safeReports);

