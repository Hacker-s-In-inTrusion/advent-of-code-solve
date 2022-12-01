use std::ops::RangeInclusive;

#[derive(Debug, Clone)]
struct Area {
    x_range: RangeInclusive<isize>,
    y_range: RangeInclusive<isize>
}

pub fn day17() {
    let input: Area = {
        let four_nums: Vec<isize> = std::fs::read_to_string("input/input17.txt")
            .unwrap()
            .replace("target area: ", "")
            .replace("x=", "")
            .replace("y=", "")
            .replace("..", " ")
            .replace(",", "")
            .split(" ")
            .map(|s| s.parse::<isize>().unwrap())
            .collect();
        
        Area { x_range: four_nums[0]..=four_nums[1], y_range: four_nums[2]..=four_nums[3] }
    };

    day17_part1(input.clone());
    day17_part2(input.clone());
}

fn day17_part1(input: Area) {
    // for every t, there exists at least one initial x velocity which can reach the target area with the given input
    // so in part1, let's simply ignore about x

    let mut highest = 0;

    for t in 1..=*input.x_range.end() {
        let float_t: f64 = t as f64;
        let lower_bound = (*input.y_range.start() as f64 / float_t + (float_t - 1.0) / 2.0).ceil() as usize;
        let upper_bound = (*input.y_range.end() as f64 / float_t + (float_t - 1.0) / 2.0).floor() as usize;

        if !(lower_bound..=upper_bound).is_empty() {
            // then there exists at least one initial x velocity which can reach the target area
            highest = highest.max((upper_bound * upper_bound + upper_bound) / 2);
        }
    }

    println!("Part One: {}", highest);
}

fn day17_part2(input: Area) {
    let mut cnt = 0;

    for x0 in 1..=*input.x_range.end() {
        for y0 in *input.y_range.start()..=1000 {
            let mut vx = x0;
            let mut vy = y0;

            let mut px = 0;
            let mut py = 0;

            loop {
                px += vx;
                py += vy;

                if input.x_range.contains(&px) && input.y_range.contains(&py) {
                    cnt += 1;
                    break;
                } else if px > *input.x_range.end() || py < *input.y_range.start() {
                    break;
                }

                if vx > 0 { vx -= 1; }
                vy -= 1;
            }
        }
    }

    println!("Part Two: {}", cnt);
}