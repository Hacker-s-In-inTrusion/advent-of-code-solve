pub fn day02() {
    let input: Vec<String> = std::fs::read_to_string("input/input02.txt")
        .unwrap()
        .lines()
        .map(|s| s.to_string())
        .collect();
    
    day02_part1(&input);
    day02_part2(&input);
}

fn day02_part1(input: &Vec<String>) {    
    let mut horizontal: i64 = 0;
    let mut depth: i64 = 0;
    for line in input.iter() {
        let (direction, value) = line.split_once(' ').unwrap();
        let value: i64 = value.parse().unwrap();

        if direction == "forward" {
            horizontal += value;
        } else if direction == "up" {
            depth -= value;
        } else if direction == "down" {
            depth += value;
        }
    }

    println!("Part One: {}", horizontal * depth);
}

fn day02_part2(input: &Vec<String>) {    
    let mut horizontal: i64 = 0;
    let mut depth: i64 = 0;
    let mut aim: i64 = 0;
    for line in input.iter() {
        let (direction, value) = line.split_once(' ').unwrap();
        let value: i64 = value.parse().unwrap();

        if direction == "forward" {
            horizontal += value;
            depth += aim * value;
        } else if direction == "up" {
            aim -= value;
        } else if direction == "down" {
            aim += value;
        }
    }

    println!("Part Two: {}", horizontal * depth);
}