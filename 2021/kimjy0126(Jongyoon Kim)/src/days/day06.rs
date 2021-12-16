pub fn day06() {
    let input: Vec<i32> = std::fs::read_to_string("input/input06.txt")
        .unwrap()
        .split(",")
        .map(|s| s.parse::<i32>().unwrap())
        .collect();

    day06_part1(input.clone());
    day06_part2(input.clone());
}

fn day06_part1(mut input: Vec<i32>) {
    const DAYS: i32 = 80;

    for _ in 0..DAYS {
        let mut create: usize = 0;
        for state in input.iter_mut() {
            if *state == 0 {
                create += 1;
                *state = 6;
            } else {
                *state -= 1;
            }
        }

        input.append(&mut vec![8; create]);
    }

    println!("Part One: {}", input.len());
}

fn day06_part2(input: Vec<i32>) {
    const DAYS: i32 = 256;
    let mut num_of_each_states: Vec<i64> = vec![0; 9];

    for state in input {
        num_of_each_states[state as usize] += 1;
    }

    for _ in 0..DAYS {
        let create: i64 = num_of_each_states[0];
        for state in 0..8 {
            num_of_each_states[state] = num_of_each_states[state + 1];
        }
        num_of_each_states[6] += create;
        num_of_each_states[8] = create;
    }

    println!("Part Two: {}", num_of_each_states.iter().sum::<i64>());
}