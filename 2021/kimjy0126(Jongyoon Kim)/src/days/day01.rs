pub fn day01() {
    let input: Vec<i32> = std::fs::read_to_string("input/input01.txt")
        .unwrap()
        .lines()
        .map(|s| s.parse::<i32>().unwrap())
        .collect();
    
    day01_part1(&input);
    day01_part2(&input);
}

fn day01_part1(input: &Vec<i32>) {
    let mut prev: Option<i32> = None;
    let mut cur: Option<i32>;
    let mut inc: i32 = 0;

    for n in input.iter() {
        cur = Some(*n);

        match prev {
            Some(p) => {
                if p < *n {
                    inc += 1;
                }
            },
            None => {}
        };

        prev = cur;
    }

    println!("Part One: {}", inc);
}

fn day01_part2(input: &Vec<i32>) {
    let mut prev3: Option<i32> = None;      // for checking if prevsum reflects three numbers
    let mut prev2: Option<i32> = None;
    let mut prev1: Option<i32> = None;
    let mut cur: Option<i32>;
    let mut prevsum: i32 = 0;
    let mut cursum: i32 = 0;
    let mut inc: i32 = 0;

    for n in input.iter() {
        cur = Some(*n);
        cursum += cur.unwrap();

        if let Some(_) = prev3 {
            if prevsum < cursum {
                inc += 1;
            }
        }

        prevsum = cursum;
        cursum -= match prev2 {
            Some(p) => p,
            None => 0
        };
        prev3 = prev2;
        prev2 = prev1;
        prev1 = cur;
    }

    println!("Part Two: {}", inc);
}