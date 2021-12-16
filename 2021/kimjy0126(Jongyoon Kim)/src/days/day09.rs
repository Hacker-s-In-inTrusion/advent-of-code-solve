pub fn day09() {
    let input: Vec<Vec<i32>> = std::fs::read_to_string("input/input09_small.txt")
        .unwrap()
        .lines()
        .map(|l| l.as_bytes().iter()
            .map(|n| (n - '0' as u8) as i32)
            .collect()
        )
        .collect();

    /* process input */
    let mut map: Vec<Vec<Option<i32>>> = vec![vec![None; input[0].len() + 2]];
    map.append(&mut input
        .iter()
        .map(|v| {
            let mut new_v = vec![None];
            new_v.append(
                &mut v
                .iter()
                .map(|n| Some(*n))
                .collect::<Vec<Option<i32>>>()
                .clone()
            );
            new_v.push(None);
            new_v
        })
        .collect::<Vec<Vec<Option<i32>>>>()
        .clone()
    );
    map.push(vec![None; input[0].len() + 2]);

    day09_part1(&map);
    day09_part2(&map);
}

fn day09_part1(map: &Vec<Vec<Option<i32>>>) {
    let row = map.len();
    let col = map[0].len();

    let get_adjacent = |r: usize, c: usize| -> Vec<Option<i32>> {
        vec![map[r - 1][c], map[r][c + 1], map[r + 1][c], map[r][c - 1]]
    };

    let mut sum = 0;
    for r in 1..(row - 1) {
        for c in 1..(col - 1) {
            let mut is_low = true;

            for adj in get_adjacent(r, c) {
                if adj != None && map[r][c].unwrap() >= adj.unwrap() {
                    is_low = false;
                    break;
                }
            }

            if is_low {
                sum += map[r][c].unwrap() + 1;
            }
        }
    }

    println!("Part One: {}", sum);
}

fn day09_part2(map: &Vec<Vec<Option<i32>>>) {
    #[derive(Debug, Copy, Clone)]
    struct Position {
        row: usize,
        col: usize
    };

    fn get_low_point(map: &Vec<Vec<Option<i32>>>) -> Vec<Position> {
        let row = map.len();
        let col = map[0].len();
    
        let get_adjacent = |r: usize, c: usize| -> Vec<Option<i32>> {
            vec![map[r - 1][c], map[r][c + 1], map[r + 1][c], map[r][c - 1]]
        };
    
        let mut low_point = vec![];
        for r in 1..(row - 1) {
            for c in 1..(col - 1) {
                let mut is_low = true;
    
                for adj in get_adjacent(r, c) {
                    if adj != None && map[r][c].unwrap() >= adj.unwrap() {
                        is_low = false;
                        break;
                    }
                }
    
                if is_low {
                    low_point.push(Position { row: r, col: c });
                }
            }
        }

        low_point
    }

    println!("{:?}", get_low_point(map));
}