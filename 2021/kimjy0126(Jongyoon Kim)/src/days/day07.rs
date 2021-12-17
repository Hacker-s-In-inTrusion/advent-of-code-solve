pub fn day07() {
    let input: Vec<i32> = std::fs::read_to_string("input/input07.txt")
        .unwrap()
        .split(",")
        .map(|s| s.parse::<i32>().unwrap())
        .collect();

    day07_part1(input.clone());
    day07_part2(input.clone());
}

fn day07_part1(mut input: Vec<i32>) {
    input.sort_unstable();

    let median = input[input.len() / 2];

    let result: i32 = input
        .iter()
        .map(|pos| (pos - median as i32).abs())
        .sum();
    
    println!("Part One: {}", result);
}

fn day07_part2(input: Vec<i32>) {
    fn presum(n: i32) -> i32 {
        n * (n + 1) / 2
    }

    /* let mut alignment_position: i32 = 0; */
    let mut result: i32 = input.iter().map(|pos| presum(*pos)).sum();
    for position in 1..=2000 {
        let res = input.iter().map(|pos| presum((pos - position).abs())).sum();
        if result > res {
            result = res;
            /* alignment_position = position; */
        }
    }

    /* proper alignment position is same with the average of positions, but I don't know why
    let avg: i32 = input.iter().sum::<i32>() / input.len() as i32;
    println!("avg position: {}", avg);
    println!("alignment position: {}", alignment_position);
    */

    println!("Part Two: {}", result);
}