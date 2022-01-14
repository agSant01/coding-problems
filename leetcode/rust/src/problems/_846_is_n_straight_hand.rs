use std::collections::BTreeMap;

#[allow(unused)]
fn is_n_straight_hand(hand: Vec<i32>, group_size: i32) -> bool {
    if group_size <= 1 {
        return true;
    }

    if hand.len() % (group_size as usize) != 0 {
        return false;
    }

    let mut cgv: Vec<(i32, i16)> = vec![(-1, 0); hand.len() / group_size as usize];
    let mut card_count: BTreeMap<i32, i32> = BTreeMap::new();

    for card in hand {
        *card_count.entry(card).or_insert(0) += 1;
    }

    let mut group: usize;
    let mut sorted_cards: Vec<i32> = card_count.keys().copied().collect();
    sorted_cards.reverse();

    while let Some(card) = sorted_cards.pop() {
        if let Some(count) = card_count.get_mut(&card) {
            if *count == 0 {
                continue;
            }

            group = 0;
            // println!("Removed card and count: {} {}", card, count);

            while *count > 0 && group < cgv.len() {
                if cgv[group].1 < group_size as i16 {
                    if cgv[group].1 == 0 || card - 1 == cgv[group].0 {
                        cgv[group].0 = card;
                        cgv[group].1 += 1;
                        *count -= 1;
                    }
                }
                // println!("card:{} | g:{} => {:?}", card, group, cgv[group]);
                group += 1;
            }

            // println!("Card:{} | Count:{}", card, count);

            if *count > 0 {
                return false;
            }
        }
    }

    // println!("CGV: {:?}", cgv);
    return true;
}

#[test]
fn test() {
    let mut hand = vec![1, 2, 3, 6, 2, 3, 4, 7, 8];
    let mut size = 3;
    let mut result = is_n_straight_hand(hand.clone(), size);
    println!("Result => {:?} {} {}", hand, size, result);
    assert_eq!(result, true);

    hand = vec![1, 2, 3, 4, 5];
    size = 4;
    result = is_n_straight_hand(hand.clone(), size);
    println!("Result => {:?} {} {}", hand, size, result);
    assert_eq!(result, false);

    hand = vec![8, 10, 12];
    size = 3;
    result = is_n_straight_hand(hand.clone(), size);
    println!("Result => {:?} {} {}", hand, size, result);
    assert_eq!(result, false);
}
