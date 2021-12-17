const SIZE: usize = 1000;

#[derive(Debug, Copy, Clone)]
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
struct Line {
    s: Position,
    e: Position
}

impl Line {
    fn new(s: Position, e: Position) -> Line {
        Line { s, e }
    }
}

pub fn day05() {
    let input: Vec<Line> = std::fs::read_to_string("input/input05.txt")
        .unwrap()
        .lines()
        .map(|s| {
            let point: Vec<Position> = s.split(" -> ")
                .map(|pos| {
                    let splitted: Vec<usize> = pos.split(",")
                    .map(|ss| ss.parse::<usize>().unwrap())
                    .collect();
                    Position::new(splitted[0], splitted[1])
                })
                .collect();
            Line::new(point[0], point[1])
        })
        .collect();
        
    /* code for calculating size of the board
    let SIZE: usize = input
        .iter()
        .map(|s| s.replace(" -> ", ",")
            .split(",")
            .map(|ss| ss.parse::<usize>().unwrap())
            .max()
            .unwrap()
        )
        .max()
        .unwrap();
    */

    day05_part1(&input);
    day05_part2(&input);
}

fn day05_part1(input: &Vec<Line>) {
    let mut map: Vec<Vec<usize>> = vec![vec![0; SIZE]; SIZE];

    let mut overlapping: i32 = 0;
    for line in input {
        if line.s.x == line.e.x {
            // vertical
            let x: usize = line.s.x;
            for y in get_range(line.s.y, line.e.y) {
                if { map[x][y] += 1; map[x][y] == 2 } {
                    overlapping += 1;
                }
            }
        } else if line.s.y == line.e.y {
            // horizontal
            let y: usize = line.s.y;
            for x in get_range(line.s.x, line.e.x) {
                if { map[x][y] += 1; map[x][y] == 2 } {
                    overlapping += 1;
                }
            }
        }
    }

    println!("Part One: {}", overlapping);
}

fn day05_part2(input: &Vec<Line>) {
    let mut map: Vec<Vec<usize>> = vec![vec![0; SIZE]; SIZE];

    let mut overlapping: i32 = 0;
    for line in input {
        if line.s.x == line.e.x {
            // vertical
            let x: usize = line.s.x;
            for y in get_range(line.s.y, line.e.y) {
                if { map[x][y] += 1; map[x][y] == 2 } {
                    overlapping += 1;
                }
            }
        } else if line.s.y == line.e.y {
            // horizontal
            let y: usize = line.s.y;
            for x in get_range(line.s.x, line.e.x) {
                if { map[x][y] += 1; map[x][y] == 2 } {
                    overlapping += 1;
                }
            }
        } else {
            // diagonal
            for (x, y) in get_range(line.s.x, line.e.x).zip(get_range(line.s.y, line.e.y)) {
                if { map[x][y] += 1; map[x][y] == 2 } {
                    overlapping += 1;
                }
            }
        }
    }

    println!("Part Two: {}", overlapping);
}

fn get_range(n1: usize, n2: usize) -> Box<dyn std::iter::Iterator<Item = usize>> {
    if n1 < n2 { Box::new(n1..=n2) } else { Box::new((n2..=n1).rev()) }
}