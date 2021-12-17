use std::collections::VecDeque;

#[derive(Debug, Copy, Clone)]
struct Position {
    row: usize,
    col: usize
}

impl Position {
    fn new(row: usize, col: usize) -> Position {
        Position { row, col }
    }
}

pub fn day11() {
    let input: Vec<Vec<u32>> = std::fs::read_to_string("input/input11.txt")
        .unwrap()
        .lines()
        .map(|line| line.chars()
            .map(|ch| ch.to_digit(10).unwrap())
            .collect()
        )
        .collect();
    
    day11_part1(&input);
    day11_part2(&input);
}

const SIZE: usize = 10;

fn day11_part1(input: &Vec<Vec<u32>>) {
    const STEPS: i32 = 100;

    let get_adjacent = |p: Position| -> Vec<Position> {
        let mut result: Vec<Position> = vec![];
        let dir_x = vec![-1, -1, -1, 0, 0, 1, 1, 1];
        let dir_y = vec![-1, 0, 1, -1, 1, -1, 0, 1];

        for (dx, dy) in dir_x.iter().zip(dir_y.iter()) {
            let prow = p.row as i32;
            let pcol = p.col as i32;

            let row = prow + dx;
            let col = pcol + dy;

            if 0 <= row && row < SIZE as i32 && 0 <= col && col < SIZE as i32 {
                result.push(Position::new(row as usize, col as usize));
            }
        }

        result
    };

    let mut map: Vec<Vec<u32>> = input.clone();

    let mut flashes = 0;
    for _ in 0..STEPS {
        let mut flash_q: VecDeque<Position> = VecDeque::new();
        let mut is_flashed: Vec<Vec<bool>> = vec![vec![false; SIZE]; SIZE];
        for r in 0..SIZE {
            for c in 0..SIZE {
                map[r][c] += 1;
                if map[r][c] > 9 {
                    // flashes
                    is_flashed[r][c] = true;
                    flash_q.push_back(Position::new(r, c));
                    flashes += 1;
                }
            }
        }

        while !flash_q.is_empty() {
            let flash_p = flash_q.pop_front().unwrap();

            let adj = get_adjacent(flash_p);
            for adj_p in adj {
                map[adj_p.row][adj_p.col] += 1;
                if map[adj_p.row][adj_p.col] > 9 && is_flashed[adj_p.row][adj_p.col] == false {
                    // flashes
                    is_flashed[adj_p.row][adj_p.col] = true;
                    flash_q.push_back(adj_p);
                    flashes += 1;
                }
            }
        }

        for r in 0..SIZE {
            for c in 0..SIZE {
                if is_flashed[r][c] == true {
                    map[r][c] = 0;
                }
            }
        }
    }

    println!("Part One: {}", flashes);
}

fn day11_part2(input: &Vec<Vec<u32>>) {
    let get_adjacent = |p: Position| -> Vec<Position> {
        let mut result: Vec<Position> = vec![];
        let dir_x = vec![-1, -1, -1, 0, 0, 1, 1, 1];
        let dir_y = vec![-1, 0, 1, -1, 1, -1, 0, 1];

        for (dx, dy) in dir_x.iter().zip(dir_y.iter()) {
            let prow = p.row as i32;
            let pcol = p.col as i32;

            let row = prow + dx;
            let col = pcol + dy;

            if 0 <= row && row < SIZE as i32 && 0 <= col && col < SIZE as i32 {
                result.push(Position::new(row as usize, col as usize));
            }
        }

        result
    };

    let mut map: Vec<Vec<u32>> = input.clone();

    let mut step = 1;
    loop {
        let mut flash_q: VecDeque<Position> = VecDeque::new();
        let mut is_flashed: Vec<Vec<bool>> = vec![vec![false; SIZE]; SIZE];
        for r in 0..SIZE {
            for c in 0..SIZE {
                map[r][c] += 1;
                if map[r][c] > 9 {
                    // flashes
                    is_flashed[r][c] = true;
                    flash_q.push_back(Position::new(r, c));
                }
            }
        }

        while !flash_q.is_empty() {
            let flash_p = flash_q.pop_front().unwrap();

            let adj = get_adjacent(flash_p);
            for adj_p in adj {
                map[adj_p.row][adj_p.col] += 1;
                if map[adj_p.row][adj_p.col] > 9 && is_flashed[adj_p.row][adj_p.col] == false {
                    // flashes
                    is_flashed[adj_p.row][adj_p.col] = true;
                    flash_q.push_back(adj_p);
                }
            }
        }

        let mut is_all_flashed = true;
        for r in 0..SIZE {
            for c in 0..SIZE {
                if is_flashed[r][c] == true {
                    map[r][c] = 0;
                } else {
                    is_all_flashed = false;
                }
            }
        }
        if is_all_flashed {
            break;
        }

        step += 1;
    }

    println!("Part Two: {}", step);
}