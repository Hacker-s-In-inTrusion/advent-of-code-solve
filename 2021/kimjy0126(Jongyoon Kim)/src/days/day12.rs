use std::collections::HashMap;

pub fn day12() {
    fn make_path_from_input(input: &Vec<(String, String)>) -> HashMap<&str, Vec<&str>> {
        let mut path: HashMap<&str, Vec<&str>> = HashMap::new();

        for line in input {
            let cave1 = path.entry(&line.0).or_insert(vec![]);
            cave1.push(&line.1);
            let cave2 = path.entry(&line.1).or_insert(vec![]);
            cave2.push(&line.0);
        }

        path
    }

    let input: Vec<(String, String)> = std::fs::read_to_string("input/input12.txt")
        .unwrap()
        .lines()
        .map(|s| {
            let splitted: Vec<&str> = s.split("-").collect();
            (splitted[0].to_string(), splitted[1].to_string())
        })
        .collect();

    let path: HashMap<&str, Vec<&str>> = make_path_from_input(&input);

    day12_part1(&path);
    day12_part2(&path);
}

fn day12_part1(path: &HashMap<&str, Vec<&str>>) {
    fn permutation<'a>(path: &HashMap<&'a str, Vec<&'a str>>, current: &'a str, mut visit: &mut HashMap<&'a str, bool>) -> i32 {
        if current == "end" {
            return 1;
        }

        if current == current.to_ascii_lowercase() {
            *visit.get_mut(current).unwrap() = true;
        }
        let result = path[current].iter().map(|next| if !visit[next] { permutation(path, next, &mut visit) } else { 0 }).sum();
        *visit.get_mut(current).unwrap() = false;

        result
    }

    let mut visit: HashMap<&str, bool> = path.keys().map(|s| *s).zip(vec![false; path.len()]).collect();

    println!("Part One: {}", permutation(path, "start", &mut visit));
}

fn day12_part2(path: &HashMap<&str, Vec<&str>>) {
    fn permutation<'a>(path: &HashMap<&'a str, Vec<&'a str>>, current: &'a str, mut visit: &mut HashMap<&'a str, bool>, chance: Option<&str>) -> i32 {
        if current == "end" {
            return 1;
        }

        if current == current.to_ascii_lowercase() {
            *visit.get_mut(current).unwrap() = true;
        }
        let result = path[current].iter().map(|next|
            if *next == "start" {
                0
            } else if !visit[next] {
                permutation(path, next, &mut visit, chance)
            } else if chance.is_none() {
                permutation(path, next, &mut visit, Some(*next))
            } else {
                0
            }
        ).sum();
        if chance != Some(current) {
            *visit.get_mut(current).unwrap() = false;
        }

        result
    }

    let mut visit: HashMap<&str, bool> = path.keys().map(|s| *s).zip(vec![false; path.len()]).collect();

    println!("Part Two: {}", permutation(path, "start", &mut visit, None));
}