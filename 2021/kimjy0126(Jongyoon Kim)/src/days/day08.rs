#[derive(Debug, Clone)]
struct Line {
    pattern: Vec<String>,
    value: Vec<String>
}

impl Line {
    fn new(pattern: Vec<String>, value: Vec<String>) -> Line {
        Line { pattern, value }
    }
}

pub fn day08() {
    let input: Vec<Line> = std::fs::read_to_string("input/input08.txt")
        .unwrap()
        .lines()
        .map(|s| {
            let splitted: Vec<Vec<String>> = s
                .split(" | ")
                .map(|ss| ss
                    .split(" ")
                    .map(|sss| sss.to_string())
                    .collect()
                )
                .collect();
            
            Line::new(splitted[0].clone(), splitted[1].clone())
        })
        .collect();
    
    day08_part1(input.clone());
    day08_part2(input.clone());
}

fn day08_part1(mut input: Vec<Line>) {
    /*
        frequencies of each segments
            a b c d e f g are in
            8 6 8 7 4 9 7 digits
    */

    for line in input.iter_mut() {
        line.pattern.sort_unstable_by(|a, b| a.len().cmp(&b.len()));
    }

    let mut cnt = 0;
    for line in input {
        let mut connect: Vec<Option<char>> = vec![None; 7];  // connect[0] == 'c' means 'a' in input is actually 'c'
        let mut frequencies: Vec<i32> = vec![0; 7];
        for pat in &line.pattern {
            for seg in pat.chars() {
                frequencies[alpha_to_digit(seg)] += 1;
            }
        }

        for (i, freq) in frequencies.iter().enumerate() {
            if *freq == 4 {
                connect[i] = Some('e');
            } else if *freq == 6 {
                connect[i] = Some('b');
            }
        }

        {   /* in case of pattern[0], which is 1 in segment */
            let pat = &line.pattern[0];

            for ch in pat.chars() {
                let digit_ch = alpha_to_digit(ch);

                if frequencies[digit_ch] == 8 {
                    connect[digit_ch] = Some('c');
                } else {
                    connect[digit_ch] = Some('f');
                }
            }
        }

        {   /* in case of pattern[1], which is 7 in segment */
            let pat = &line.pattern[1];

            for ch in pat.chars() {
                let digit_ch = alpha_to_digit(ch);

                if connect[digit_ch] == None {
                    connect[digit_ch] = Some('a');
                    break;
                }
            }
        }

        {   /* in case of pattern[2], which is 4 in segment */
            let pat = &line.pattern[2];

            for ch in pat.chars() {
                let digit_ch = alpha_to_digit(ch);

                if connect[digit_ch] == None {
                    connect[digit_ch] = Some('d');
                    break;
                }
            }
        }

        {   /* rest one is 'g' */
            for con in connect.iter_mut() {
                if *con == None {
                    *con = Some('g');
                }
            }
        }

        for value in &line.value {
            let mut segment: Vec<char> = vec![];
            for ch in value.chars() {
                segment.push(connect[alpha_to_digit(ch)].unwrap());
            }
            segment.sort_unstable_by(|a, b| a.cmp(b));
            let segment: String = String::from_iter(segment);
            if vec![1, 4, 7, 8].contains(&segment_to_digit(&segment)) {
                cnt += 1;
            }
        }
    }

    println!("Part One: {}", cnt);
}

fn day08_part2(mut input: Vec<Line>) {
    for line in input.iter_mut() {
        line.pattern.sort_unstable_by(|a, b| a.len().cmp(&b.len()));
    }

    let mut sum = 0;
    for line in input {
        let mut connect: Vec<Option<char>> = vec![None; 7];  // connect[0] == 'c' means 'a' in input is actually 'c'
        let mut frequencies: Vec<i32> = vec![0; 7];
        for pat in &line.pattern {
            for seg in pat.chars() {
                frequencies[alpha_to_digit(seg)] += 1;
            }
        }

        for (i, freq) in frequencies.iter().enumerate() {
            if *freq == 4 {
                connect[i] = Some('e');
            } else if *freq == 6 {
                connect[i] = Some('b');
            }
        }

        {   /* in case of pattern[0], which is 1 in segment */
            let pat = &line.pattern[0];

            for ch in pat.chars() {
                let digit_ch = alpha_to_digit(ch);

                if frequencies[digit_ch] == 8 {
                    connect[digit_ch] = Some('c');
                } else {
                    connect[digit_ch] = Some('f');
                }
            }
        }

        {   /* in case of pattern[1], which is 7 in segment */
            let pat = &line.pattern[1];

            for ch in pat.chars() {
                let digit_ch = alpha_to_digit(ch);

                if connect[digit_ch] == None {
                    connect[digit_ch] = Some('a');
                    break;
                }
            }
        }

        {   /* in case of pattern[2], which is 4 in segment */
            let pat = &line.pattern[2];

            for ch in pat.chars() {
                let digit_ch = alpha_to_digit(ch);

                if connect[digit_ch] == None {
                    connect[digit_ch] = Some('d');
                    break;
                }
            }
        }

        {   /* rest one is 'g' */
            for con in connect.iter_mut() {
                if *con == None {
                    *con = Some('g');
                }
            }
        }

        let mut v = 0;
        for value in &line.value {
            let mut segment: Vec<char> = vec![];
            for ch in value.chars() {
                segment.push(connect[alpha_to_digit(ch)].unwrap());
            }
            segment.sort_unstable_by(|a, b| a.cmp(b));
            let segment: String = String::from_iter(segment);

            v *= 10;
            v += segment_to_digit(&segment);
        }

        sum += v;
    }

    println!("Part Two: {}", sum);
}

fn alpha_to_digit(ch: char) -> usize {
    ch as usize - 'a' as usize
}

fn segment_to_digit(seg: &str) -> i32 {
    match seg {
        "abcefg" => 0,
        "cf" => 1,
        "acdeg" => 2,
        "acdfg" => 3,
        "bcdf" => 4,
        "abdfg" => 5,
        "abdefg" => 6,
        "acf" => 7,
        "abcdefg" => 8,
        "abcdfg" => 9,
        _ => -1
    }
}