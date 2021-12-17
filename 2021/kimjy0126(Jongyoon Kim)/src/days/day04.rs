pub fn day04() {
    let input: Vec<String> = std::fs::read_to_string("input/input04.txt")
        .unwrap()
        .replace("\r", "")
        .split("\n\n")
        .map(|s| s.to_string())
        .collect();
    
    let order: Vec<i32> = input[0]
        .split(",")
        .map(|n| n.parse::<i32>().unwrap())
        .collect();

    let boards: Vec<Vec<Vec<(i32, bool)>>> = input[1..].to_vec()
        .into_iter()
        .map(|s| s.split("\n")
            .map(|ss| ss.split_whitespace()
                .map(|sss| (sss.parse::<i32>().unwrap(), false))
                .collect())
            .collect())
        .collect();
    
    day04_part1(&order, boards.clone());
    day04_part2(&order, boards.clone());
}

const SIZE: usize = 5;

fn day04_part1(order: &Vec<i32>, mut boards: Vec<Vec<Vec<(i32, bool)>>>) {
    let mut answer: i32 = 0;

    'outer: for num in order {
        for board in &mut boards {
            for r in 0..SIZE {
                for c in 0..SIZE {
                    if board[r][c].0 == *num {
                        board[r][c].1 = true;
                        if check_bingo(&board) == true {
                            answer = get_score(&board, *num);
                            break 'outer;
                        }
                    }
                }
            }
        }
    }

    println!("Part One: {}", answer);
}

fn day04_part2(order: &Vec<i32>, mut boards: Vec<Vec<Vec<(i32, bool)>>>) {
    let mut answer: i32 = 0;

    'outer: for num in order {
        let mut win_board: Vec<usize> = vec![];

        for board_idx in 0..boards.len() {
            for r in 0..SIZE {
                for c in 0..SIZE {
                    if boards[board_idx][r][c].0 == *num {
                        boards[board_idx][r][c].1 = true;
                        if check_bingo(&boards[board_idx]) == true {
                            win_board.push(board_idx);
                        }
                    }
                }
            }
        }

        for win_board_idx in win_board.into_iter().rev() {
            if boards.len() == 1 {
                answer = get_score(&boards[0], *num);
                break 'outer;
            }

            boards.remove(win_board_idx);
        }
    }

    println!("Part Two: {}", answer);
}

fn check_bingo(board: &Vec<Vec<(i32, bool)>>) -> bool {
    for i in 0..SIZE {
        let mut is_row_bingo: bool = true;
        let mut is_col_bingo: bool = true;
        for j in 0..SIZE {
            if board[i][j].1 == false {
                is_row_bingo = false;
            }
            if board[j][i].1 == false {
                is_col_bingo = false;
            }
        }

        if is_row_bingo == true {
            return true;
        }
        if is_col_bingo == true {
            return true;
        }
    }

    false
}

fn get_score(board: &Vec<Vec<(i32, bool)>>, last_num: i32) -> i32 {
    let mut sum: i32 = 0;
    for r in 0..SIZE {
        for c in 0..SIZE {
            let (n, chk) = board[r][c];
            if chk == false {
                sum += n
            }
        }
    }

    sum * last_num
}