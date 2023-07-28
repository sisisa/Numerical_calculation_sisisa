function runBinarySearch() {
  let sortedArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  let target = 8;
  let startIndex = 0;
  let endIndex = sortedArray.length - 1;

  while (startIndex <= endIndex) {
    let middleIndex = Math.floor((startIndex + endIndex) / 2);
    if (sortedArray[middleIndex] === target) {
      console.log(`Found target ${target} at index ${middleIndex}.`);
      return;
    }
    if (sortedArray[middleIndex] < target) {
      startIndex = middleIndex + 1;
    } else {
      endIndex = middleIndex - 1;
    }
  }
  console.log(`Target ${target} not found in the array.`);
}
