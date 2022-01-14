#![allow(unused)]

fn peak_index_in_mountain_array(arr: Vec<i32>) -> i32 {
    if arr.len() <= 2 {
        return -1;
    }
    let mut i: usize = arr.len() / 2;

    while i > 0 && i < arr.len() {
        if arr[i - 1] < arr[i] && arr[i] > arr[i + 1] {
            return i as i32;
        }

        if arr[i] < arr[i + 1] {
            i += 1;
        } else {
            i -= 1;
        }
    }

    return -1;
}

#[test]
fn test() {
    assert_eq!(1, peak_index_in_mountain_array(vec![0, 1, 0]));
    println!("Res1");
    assert_eq!(1, peak_index_in_mountain_array(vec![0, 2, 1, 0]));
    println!("Res2");
    assert_eq!(1, peak_index_in_mountain_array(vec![0, 10, 5, 0]));
    println!("Res3");
    assert_eq!(3, peak_index_in_mountain_array(vec![0, 5, 5, 10, 0]));
    println!("Res4");
}
