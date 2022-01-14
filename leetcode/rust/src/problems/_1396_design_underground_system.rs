#![allow(unused)]

use std::collections::HashMap;

struct UndergroundSystem {
    station_times: HashMap<(String, String), (f64, i32)>,
    current_passengers: HashMap<i32, (String, i32)>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl UndergroundSystem {
    fn new() -> Self {
        return Self {
            station_times: HashMap::new(),
            current_passengers: HashMap::new(),
        };
    }

    // O(1)
    fn check_in(&mut self, id: i32, station_name: String, t: i32) {
        self.current_passengers.insert(id, (station_name, t));
    }

    // O(1)
    fn check_out(&mut self, id: i32, station_name: String, t: i32) {
        if let Some((entry_station, entry_time)) = self.current_passengers.get(&id) {
            let (ave_time, samples) = self
                .station_times
                .entry((entry_station.to_string(), station_name))
                .or_default();

            // Calculate rolling average

            // prev_ave * samples
            let curr_ave = *ave_time * (*samples as f64);
            // increment samples
            *samples += 1;

            // new ave = ((Prev*Count) + NewVal) / (Count+1)
            *ave_time = (curr_ave + (t - entry_time) as f64) / (*samples as f64);
        }
    }

    // O(1)
    fn get_average_time(&self, start_station: String, end_station: String) -> f64 {
        if let Some((ave_time, _)) = self.station_times.get(&(start_station, end_station)) {
            return *ave_time;
        }
        0.0
    }
}

//  Your UndergroundSystem object will be instantiated and called as such:
//  let obj = UndergroundSystem::new();
//  obj.check_in(id, stationName, t);
//  obj.check_out(id, stationName, t);
//  let ret_3: f64 = obj.get_average_time(startStation, endStation);

#[test]
fn test() {
    let mut underground_system: UndergroundSystem = UndergroundSystem::new();
    underground_system.check_in(10, String::from("Leyton"), 3);
    underground_system.check_out(10, String::from("Paradise"), 8); // Customer 10 String::from("Leyton") -> String::from("Paradise") in 8-3 = 5

    let r1 = underground_system.get_average_time(String::from("Leyton"), String::from("Paradise")); // return 5.00000, (5) / 1 = 5
    assert_eq!(r1, 5.0);

    underground_system.check_in(5, String::from("Leyton"), 10);
    underground_system.check_out(5, String::from("Paradise"), 16); // Customer 5 String::from("Leyton") -> String::from("Paradise") in 16-10 = 6

    let r2 = underground_system.get_average_time(String::from("Leyton"), String::from("Paradise")); // return 5.50000, (5 + 6) / 2 = 5.5
    assert_eq!(r2, 5.5);

    underground_system.check_in(2, String::from("Leyton"), 21);
    underground_system.check_out(2, String::from("Paradise"), 30); // Customer 2 String::from("Leyton") -> String::from("Paradise") in 30-21 = 9
    let r3 = underground_system.get_average_time(String::from("Leyton"), String::from("Paradise"));
    assert_eq!(r3, 20.0 / 3.0); // return 6.66667, (5 + 6 + 9) / 3 = 6.66667
}
