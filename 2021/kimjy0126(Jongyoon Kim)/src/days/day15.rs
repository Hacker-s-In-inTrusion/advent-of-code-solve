use std::collections::BinaryHeap;
use std::cmp::Reverse;      // for making min heap, read this: https://doc.rust-lang.org/std/collections/binary_heap/struct.BinaryHeap.html#min-heap

#[derive(Debug, Copy, Clone, PartialEq, Eq, PartialOrd, Ord)]
struct State {
    cost: u32,
    pos: Position
}

#[derive(Debug, Copy, Clone, PartialEq, Eq, PartialOrd, Ord)]
struct Position {
    row: usize,
    col: usize
}

pub fn day15() {
    let input: Vec<Vec<u32>> = std::fs::read_to_string("input/input15.txt")
        .unwrap()
        .lines()
        .map(|line| line
            .chars()
            .map(|ch| ch.to_digit(10).unwrap())
            .collect()
        )
        .collect();

    day15_part1(input.clone());
    day15_part2(input.clone());
}

const SIZE: usize = 100;

fn day15_part1(input: Vec<Vec<u32>>) {
    let get_adjacent_state = |current_state: State| -> Vec<State> {
        let dir = [(-1, 0), (0, 1), (1, 0), (0, -1)];
        let mut adj: Vec<State> = vec![];

        for d in dir {
            let new_row = current_state.pos.row as isize + d.0;
            let new_col = current_state.pos.col as isize + d.1;
    
            if (0..SIZE as isize).contains(&new_row) && (0..SIZE as isize).contains(&new_col) {
                let new_row = new_row as usize;
                let new_col = new_col as usize;
                let new_state = State { cost: current_state.cost + input[new_row][new_col],
                                        pos: Position { row: new_row, col: new_col }};
                adj.push(new_state);
            }
        }

        adj
    };

    let mut cost: Vec<Vec<Option<u32>>> = vec![vec![None; SIZE]; SIZE];
    cost[0][0] = Some(0);

    let mut current_state: State = State { cost: 0, pos: Position { row: 0, col: 0 }};
    let mut next_state: BinaryHeap<Reverse<State>> = BinaryHeap::new();
    let final_pos = Position { row: SIZE - 1, col: SIZE - 1 };
    while current_state.pos != final_pos {
        let adj = get_adjacent_state(current_state);

        for adj_state in adj {
            if cost[adj_state.pos.row][adj_state.pos.col].is_some() {
                // already visited
                continue;
            }

            next_state.push(Reverse(adj_state));
            cost[adj_state.pos.row][adj_state.pos.col] = Some(adj_state.cost);
        }

        if let Some(Reverse(ns)) = next_state.pop() {
            current_state = ns;
        }
    }

    println!("Part One: {}", cost[SIZE - 1][SIZE - 1].unwrap());
}

fn day15_part2(mut input: Vec<Vec<u32>>) {
    const EXTENDED_SIZE: usize = SIZE * 5;

    fn extend_input(input: &mut Vec<Vec<u32>>) {
        *input = input
            .iter()
            .map(|v| {
                let mut new_v: Vec<u32> = v.clone();

                for i in 1..=4 {
                    new_v.append(&mut v.iter().map(|n| n + i).collect());
                }

                new_v
            })
            .collect();

        for i in 1..=4 {
            for j in 0..SIZE {
                input.push(input[j].iter().map(|n| n + i).collect());
            }
        }

        *input = input
            .iter()
            .map(|v|
                v.iter().map(|&n| if n > 9 { n - 9 } else { n }).collect()
            )
            .collect();
    }

    extend_input(&mut input);

    let get_adjacent_state = |current_state: State| -> Vec<State> {
        let dir = [(-1, 0), (0, 1), (1, 0), (0, -1)];
        let mut adj: Vec<State> = vec![];

        for d in dir {
            let new_row = current_state.pos.row as isize + d.0;
            let new_col = current_state.pos.col as isize + d.1;
    
            if (0..EXTENDED_SIZE as isize).contains(&new_row) && (0..EXTENDED_SIZE as isize).contains(&new_col) {
                let new_row = new_row as usize;
                let new_col = new_col as usize;
                let new_state = State { cost: current_state.cost + input[new_row][new_col],
                                        pos: Position { row: new_row, col: new_col }};
                adj.push(new_state);
            }
        }

        adj
    };

    let mut cost: Vec<Vec<Option<u32>>> = vec![vec![None; EXTENDED_SIZE]; EXTENDED_SIZE];
    cost[0][0] = Some(0);

    let mut current_state: State = State { cost: 0, pos: Position { row: 0, col: 0 }};
    let mut next_state: BinaryHeap<Reverse<State>> = BinaryHeap::new();
    let final_pos = Position { row: EXTENDED_SIZE - 1, col: EXTENDED_SIZE - 1 };
    while current_state.pos != final_pos {
        let adj = get_adjacent_state(current_state);

        for adj_state in adj {
            if cost[adj_state.pos.row][adj_state.pos.col].is_some() {
                // already visited
                continue;
            }

            next_state.push(Reverse(adj_state));
            cost[adj_state.pos.row][adj_state.pos.col] = Some(adj_state.cost);
        }

        if let Some(Reverse(ns)) = next_state.pop() {
            current_state = ns;
        }
    }

    println!("Part Two: {}", cost[EXTENDED_SIZE - 1][EXTENDED_SIZE - 1].unwrap());
}