pub fn day03() {
    let input: Vec<String> = std::fs::read_to_string("input/input03.txt")
        .unwrap()
        .lines()
        .map(|s| s.to_string())
        .collect();

    day03_part1(&input);
    day03_part2(&input);
}

fn day03_part1(input: &Vec<String>) {
    let mut number_of_zeroes: Vec<i32> = vec![];
    let mut number_of_ones: Vec<i32> = vec![];

    let length: i32 = input[0].len() as i32;

    for _ in 0..length {
        number_of_zeroes.push(0);
        number_of_ones.push(0);
    }

    for s in input {
        for (i, ch) in s.chars().enumerate() {
            match ch {
                '0' => number_of_zeroes[i] += 1,
                '1' => number_of_ones[i] += 1,
                _ => ()
            };
        }
    }

    let mut gamma_rate: i32 = 0;
    for (zero, one) in number_of_zeroes.iter().zip(number_of_ones.iter()) {
        gamma_rate *= 2;
        if zero < one {
            gamma_rate += 1;
        }
    }

    let epsilon_rate = 2_i32.pow(length as u32) - 1 - gamma_rate;

    println!("Part One: {}", gamma_rate * epsilon_rate);
}

fn day03_part2(input: &Vec<String>) {
    let length: i32 = input[0].len() as i32;
    let mut oxy_pool: Vec<String> = input.clone();
    let mut co2_pool: Vec<String> = input.clone();

    /* oxy rating */
    for i in 0..length {
        let mut zeroes: i32 = 0;
        let mut ones: i32 = 0;
        for s in &oxy_pool {
            match s.as_bytes()[i as usize] as char {
                '0' => zeroes += 1,
                '1' => ones += 1,
                _ => ()
            };
        }

        let selected: char = if zeroes > ones { '0' } else { '1' };

        oxy_pool = oxy_pool
            .into_iter()
            .filter(|s| s.as_bytes()[i as usize] as char == selected)
            .collect();

        if oxy_pool.len() == 1 {
            break;
        }
    }

    /* co2 rating */
    for i in 0..length {
        let mut zeroes: i32 = 0;
        let mut ones: i32 = 0;
        for s in &co2_pool {
            match s.as_bytes()[i as usize] as char {
                '0' => zeroes += 1,
                '1' => ones += 1,
                _ => ()
            };
        }

        let selected: char = if zeroes > ones { '1' } else { '0' };

        co2_pool = co2_pool
            .into_iter()
            .filter(|s| s.as_bytes()[i as usize] as char == selected)
            .collect();

        if co2_pool.len() == 1 {
            break;
        }
    }

    let oxy_rate: i32 = i32::from_str_radix(&oxy_pool[0], 2).unwrap();
    let co2_rate: i32 = i32::from_str_radix(&co2_pool[0], 2).unwrap();

    println!("Part Two: {}", oxy_rate * co2_rate);
}