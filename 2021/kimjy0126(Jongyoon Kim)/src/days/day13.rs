#[derive(Debug, Copy, Clone, PartialEq, Eq, PartialOrd, Ord)]
struct Position {
    x: usize,
    y: usize
}

impl Position {
    fn new(x: usize, y: usize) -> Position {
        Position { x, y }
    }
}

#[derive(Debug, Copy, Clone)]
enum Line {
    X(usize),
    Y(usize)
}

pub fn day13() {
    let input: Vec<String> = std::fs::read_to_string("input/input13.txt")
        .unwrap()
        .replace("\r", "")
        .split("\n\n")
        .map(|s| s.to_string())
        .collect();

    // process input
    let dots: Vec<Position> = input[0]
        .lines()
        .map(|line| {
            let p: Vec<usize> = line.split(",").map(|n| n.parse::<usize>().unwrap()).collect();
            Position::new(p[0], p[1])
        })
        .collect();
    
    let folding_lines: Vec<Line> = input[1]
        .lines()
        .map(|line| {
            let processed_line: Vec<String> = line.replace("fold along ", "").split("=").map(|s| s.to_string()).collect();
            let n = processed_line[1].parse::<usize>().unwrap();

            if processed_line[0] == "x" {
                Line::X(n)
            } else {
                Line::Y(n)
            }
        })
        .collect();

    day13_part1(dots.clone(), folding_lines.clone());
    day13_part2(dots.clone(), folding_lines.clone());
}

fn day13_part1(mut dots: Vec<Position>, folding_lines: Vec<Line>) {
    match folding_lines[0] {
        Line::X(x) => {
            for dot in dots.iter_mut() {
                if dot.x > x {
                    dot.x = 2 * x - dot.x;
                }
            }
        },
        Line::Y(y) => {
            for dot in dots.iter_mut() {
                if dot.y > y {
                    dot.y = 2 * y - dot.y;
                }
            }
        }
    }

    dots.sort();
    dots.dedup();

    println!("Part One: {}", dots.len());
}

fn day13_part2(mut dots: Vec<Position>, folding_lines: Vec<Line>) {
    for line in folding_lines {
        match line {
            Line::X(x) => {
                for dot in dots.iter_mut() {
                    if dot.x > x {
                        dot.x = 2 * x - dot.x;
                    }
                }
            },
            Line::Y(y) => {
                for dot in dots.iter_mut() {
                    if dot.y > y {
                        dot.y = 2 * y - dot.y;
                    }
                }
            }
        }
    }

    dots.sort();
    dots.dedup();

    let x_max = dots.iter().map(|dot| dot.x).max().unwrap();
    let x_min = dots.iter().map(|dot| dot.x).min().unwrap();
    let y_max = dots.iter().map(|dot| dot.y).max().unwrap();
    let y_min = dots.iter().map(|dot| dot.y).min().unwrap();
    let mut final_map: Vec<Vec<char>> = vec![vec!['.'; x_max - x_min + 1]; y_max - y_min + 1];

    for dot in dots.iter() {
        final_map[dot.y - y_min][dot.x - x_min] = '#';
    }

    println!("Part Two:");
    for line in final_map {
        for ch in line {
            print!("{}", ch);
        }
        println!();
    }
}