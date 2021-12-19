use std::collections::HashMap;

pub fn day14() {
    let input: Vec<String> = std::fs::read_to_string("input/input14.txt")
        .unwrap()
        .replace("\r", "")
        .split("\n\n")
        .map(|s| s.to_string())
        .collect();

    // process input
    let polymer_template: String = input[0].clone();
    let rules: HashMap<String, char> = input[1]
        .lines()
        .map(|line| {
            let splitted_line: Vec<&str> = line.split(" -> ").collect();
            
            let from: String = splitted_line[0].to_string();
            let to: char = splitted_line[1].chars().nth(0).unwrap();

            (from, to)
        })
        .collect();

    day14_part1(polymer_template.clone(), rules.clone());
    day14_part2(polymer_template.clone(), rules.clone());
}

fn day14_part1(mut polymer: String, rules: HashMap<String, char>) {
    const STEP: usize = 10;

    for _ in 0..STEP {
        let mut next_polymer: String = String::new();

        for i in 0..polymer.len() - 1 {
            let slice = &polymer[i..=i + 1];

            next_polymer.push(slice.chars().nth(0).unwrap());
            if let Some(to) = rules.get(slice) {
                next_polymer.push(*to);
            }
        }

        next_polymer.push(polymer.chars().last().unwrap());

        polymer = next_polymer;
    }
    
    let mut alpha_freq: HashMap<char, usize> = HashMap::new();

    for ch in polymer.chars() {
        if alpha_freq.get(&ch) == None {
            alpha_freq.insert(ch, 0);
        }

        *alpha_freq.get_mut(&ch).unwrap() += 1;
    }

    println!("Part One: {}", alpha_freq.values().max().unwrap() - alpha_freq.values().min().unwrap());
}

fn day14_part2(polymer: String, rules: HashMap<String, char>) {
    const STEP: usize = 40;

    let mut alpha_freq: HashMap<char, usize> = HashMap::new();
    alpha_freq.insert(polymer.chars().nth(0).unwrap(), 1);
    alpha_freq.insert(polymer.chars().last().unwrap(), 1);

    let mut pairs: HashMap<String, usize> = HashMap::new();
    for i in 0..polymer.len() - 1 {
        let slice = &polymer[i..=i + 1];

        if pairs.get(slice) == None {
            pairs.insert(slice.to_string(), 0);
        }

        *pairs.get_mut(slice).unwrap() += 1;
    }

    // rules is shadowed here!
    let rules: HashMap<String, Vec<String>> = rules
        .iter()
        .map(|(from, to)| {
            let to1 = [from.chars().nth(0).unwrap(), *to].to_vec().iter().collect();
            let to2 = [*to, from.chars().last().unwrap()].to_vec().iter().collect();

            (from.clone(), vec![to1, to2])
        })
        .collect();

    for _ in 0..STEP {
        let mut next_pairs: HashMap<String, usize> = HashMap::new();

        for (key, val) in pairs.iter() {
            let mut to_push: Vec<String> = vec![];

            match &rules.get(key) {
                Some(v) => to_push = v.to_vec(),
                None => to_push.push(key.clone())
            };

            for push_str in to_push {
                if next_pairs.get(&push_str) == None {
                    next_pairs.insert(push_str, *val);
                } else {
                    *next_pairs.get_mut(&push_str).unwrap() += val;
                }
            }
        }

        pairs = next_pairs;
    }

    for (key, val) in pairs.iter() {
        for ch in key.chars() {
            if alpha_freq.get(&ch) == None {
                alpha_freq.insert(ch, *val);
            } else {
                *alpha_freq.get_mut(&ch).unwrap() += val;
            }
        }
    }

    for (_, val) in alpha_freq.iter_mut() {
        *val /= 2;
    }

    println!("Part Two: {}", alpha_freq.values().max().unwrap() - alpha_freq.values().min().unwrap());
}