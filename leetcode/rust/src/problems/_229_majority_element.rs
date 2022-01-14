use std::collections::BTreeMap;

#[allow(unused)]
fn majority_element(nums: Vec<i32>) -> Vec<i32> {
    let mut map: BTreeMap<i32, i32> = BTreeMap::new();

    let target: i32 = nums.len() as i32 / 3;
    for num in nums.into_iter() {
        *map.entry(num).or_insert(0) += 1;
    }

    map.iter()
        .filter(|(_, &count)| count > target)
        .map(|(&num, _)| num)
        .collect()
}

#[test]
fn test() {
    // Input: nums = [3,2,3]
    // Output: [3]
    let mut nums = vec![3, 2, 3];
    assert_eq!(vec![3], majority_element(nums.clone()));

    // Input: nums = [1]
    // Output: [1]
    nums = vec![1];
    assert_eq!(vec![1], majority_element(nums.clone()));

    // Input: nums = [1,2]
    // Output: [1,2]
    nums = vec![1, 2];
    assert_eq!(vec![1, 2], majority_element(nums.clone()));
}
