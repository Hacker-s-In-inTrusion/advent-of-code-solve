pub fn day10() {
    let input: Vec<String> = std::fs::read_to_string("input/input10.txt")
        .unwrap()
        .lines()
        .map(|s| s.to_string())
        .collect();
    
    day10_part1(input.clone());
    day10_part2(input.clone());
}

fn day10_part1(input: Vec<String>) {
    let score = vec![3, 57, 1197, 25137];
    let mut illegal_cnt = vec![0; 4];

    for line in &input {
        let mut bracket_stack = vec![];

        for ch in line.chars() {
            let bracket_num = bracket_to_num(ch);

            if is_bracket_open(ch) {
                bracket_stack.push(bracket_num);
            } else if !bracket_stack.is_empty() && bracket_stack.pop().unwrap() == bracket_num {
                // already did something in condition checking
            } else {
                // found illegal bracket
                illegal_cnt[bracket_num] += 1;
                break;
            }
        }
    }

    println!("Part One: {}", score.iter().zip(illegal_cnt.iter()).map(|(a, b)| a * b).sum::<i32>());
}

fn day10_part2(input: Vec<String>) {
    let score = vec![1, 2, 3, 4];
    let mut total_score = vec![];

    'outer: for line in &input {
        let mut bracket_stack = vec![];

        for ch in line.chars() {
            let bracket_num = bracket_to_num(ch);

            if is_bracket_open(ch) {
                bracket_stack.push(bracket_num);
            } else if !bracket_stack.is_empty() && bracket_stack.pop().unwrap() == bracket_num {
                // already did something in condition checking
            } else {
                // corrupted line
                continue 'outer;
            }
        }

        let mut line_score: i64 = 0;
        while !bracket_stack.is_empty() {
            line_score *= 5;
            line_score += score[bracket_stack.pop().unwrap()];
        }
        total_score.push(line_score);
    }

    total_score.sort();

    println!("Part Two: {}", total_score[total_score.len() / 2]);
}

fn is_bracket_open(bracket: char) -> bool {
    match bracket {
        '(' | '[' | '{' | '<' => true,
        _ => false,
    }
}

fn bracket_to_num(bracket: char) -> usize {
    match bracket {
        '(' | ')' => 0,
        '[' | ']' => 1,
        '{' | '}' => 2,
        '<' | '>' => 3,
        _ => 4
    }
}