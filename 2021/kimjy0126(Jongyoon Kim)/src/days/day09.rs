pub fn day09() {
    let input: Vec<Vec<i32>> = std::fs::read_to_string("input/input09.txt")
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

    // Q. why is this closure not function?
    // A. for capturing map, instead of giving as parameter
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
    use std::collections::VecDeque;

    #[derive(Debug, Copy, Clone)]
    struct Position {
        row: usize,
        col: usize
    }

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

    // Q. why is this closure not function?
    // A. for capturing map, instead of giving as parameter
    let get_adjacent_pos = |p: &Position| -> Vec<Position> {
        let (r, c) = (p.row, p.col);
        vec![Position { row: r - 1, col: c }, Position { row: r, col: c + 1}, Position { row: r + 1, col: c }, Position { row: r, col: c - 1 }]
    };

    let low_point: Vec<Position> = get_low_point(map);
    let num_of_basin = get_low_point(map).len();
    let mut basin_area = vec![1; num_of_basin];

    let row = map.len();
    let col = map[0].len();
    let mut map_basin: Vec<Vec<Option<i32>>> = vec![vec![None; col]; row];
    for (i, p) in low_point.iter().enumerate() {
        map_basin[p.row][p.col] = Some(i as i32);
    }

    let mut pos_q: VecDeque<Position> = VecDeque::from(low_point);
    while !pos_q.is_empty() {
        let target_p = pos_q.pop_front().unwrap();
        let adj = get_adjacent_pos(&target_p);

        for adj_p in &adj {
            if map[adj_p.row][adj_p.col].is_some() {
                if map[adj_p.row][adj_p.col].unwrap() < 9
                        && map[adj_p.row][adj_p.col].unwrap() > map[target_p.row][target_p.col].unwrap()
                        && map_basin[adj_p.row][adj_p.col].is_none() {
                    map_basin[adj_p.row][adj_p.col] = map_basin[target_p.row][target_p.col];
                    basin_area[map_basin[adj_p.row][adj_p.col].unwrap() as usize] += 1;
                    pos_q.push_back(*adj_p);
                }
            }
        }
    }

    basin_area.sort();
    basin_area.reverse();

    println!("Part Two: {}", basin_area[0] * basin_area[1] * basin_area[2]);
}