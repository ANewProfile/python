import { readFile } from 'fs/promises';

const parse = (input) => {
    let trimmedInput = input.trimEnd();
    let lines = trimmedInput.split("\n");
    let nums = [];
    for (let i = 0; i < lines.length; i++) {
        let splitline = lines[i].split("   ");
        nums.push(splitline[0]);
        nums.push(splitline[1]);
    }

    let leftList = [];
    let rightList = [];

    for (let i = 0; i < nums.length; i++) {
        if (i % 2 === 0) {
            leftList.push(nums[i])
        } else {
            rightList.push(nums[i])
        }
    }

    return [leftList, rightList]
}

const getOccurrences = (arr, item) => {
    var n = 0;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === item) { n++ }
    }
    return n;
}

// Read and parse input
let input = await readFile("/Users/littletheo/non-git/aoc-2024/day1input.txt", "utf8");
let [leftList, rightList] = parse(input);

// Sort and count dist btwn leftList and rightList
leftList.sort((a, b) => a - b);
rightList.sort((a, b) => a - b);

let total = 0;

for (let i = 0; i < leftList.length; i++) {
    let dist = Math.abs(leftList[i] - rightList[i]);
    total += dist;
}

// Count similarity btwn leftList and rightList
let simScore = 0;
for (let i = 0; i < leftList.length; i++) {
    let numOccurrences = getOccurrences(rightList, leftList[i]);
    simScore += leftList[i] * numOccurrences;
}

console.log(simScore);

