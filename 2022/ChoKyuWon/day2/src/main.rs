struct Round {
    score: u64,
    oppenent: char,
    guide: char,
}

impl Round {
    fn new(input: &str) -> Self {
        let mut out = Round {
            score: 0,
            oppenent: '0',
            guide: '0',
        };
        match input {
            "A X" => {
                out.oppenent = 'A';
                out.guide = 'X';
            }
            "A Y" => {
                out.oppenent = 'A';
                out.guide = 'Y';
            }
            "A Z" => {
                out.oppenent = 'A';
                out.guide = 'Z';
            }
            "B X" => {
                out.oppenent = 'B';
                out.guide = 'X';
            }
            "B Y" => {
                out.oppenent = 'B';
                out.guide = 'Y';
            }
            "B Z" => {
                out.oppenent = 'B';
                out.guide = 'Z';
            }
            "C X" => {
                out.oppenent = 'C';
                out.guide = 'X';
            }
            "C Y" => {
                out.oppenent = 'C';
                out.guide = 'Y';
            }
            "C Z" => {
                out.oppenent = 'C';
                out.guide = 'Z';
            }
            _ => panic!("WTF?"),
        };
        out
    }
    fn process(&mut self) {
        self.score += match self.guide {
            'X' => 0 + Round::char2score(&Round::losechar(&self.oppenent)),
            'Y' => 3 + Round::char2score(&self.oppenent),
            'Z' => 6 + Round::char2score(&Round::winchar(&self.oppenent)),
            _ => panic!(),
        };
    }
    fn losechar(x: &char) -> char {
        match x {
            'A' => 'C',
            'B' => 'A',
            'C' => 'B',
            _ => panic!(),
        }
    }
    fn winchar(x: &char) -> char {
        match x {
            'A' => 'B',
            'B' => 'C',
            'C' => 'A',
            _ => panic!(),
        }
    }
    fn char2score(x: &char) -> u64 {
        match x {
            'A' => 1,
            'B' => 2,
            'C' => 3,
            _ => panic!(),
        }
    }
}

fn main() {
    a();
    b();
}
fn a() {
    let input = include_str!("../input.txt").lines();
    let mut total = 0;
    for line in input {
        total += match line {
            "A X" => 1 + 3,
            "A Y" => 2 + 6,
            "A Z" => 3 + 0,
            "B X" => 1 + 0,
            "B Y" => 2 + 3,
            "B Z" => 3 + 6,
            "C X" => 1 + 6,
            "C Y" => 2 + 0,
            "C Z" => 3 + 3,
            _ => panic!("WTF?"),
        };
    }
    println!("{}", total);
}

fn b() {
    let input = include_str!("../input.txt").lines();
    let mut v: Vec<Round> = Vec::<Round>::new();
    for line in input {
        let mut elem = Round::new(line);
        elem.process();
        v.push(elem);
    }
    let total: u64 = v.iter().map(|round| round.score).sum();
    println!("{}", total);
}
