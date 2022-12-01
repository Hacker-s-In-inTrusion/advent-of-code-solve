fn main() {
    solution();
}

#[derive(PartialEq, Eq, PartialOrd, Ord)]
struct Elf {
    calrories : u64,
}
impl Elf {
    fn new(cal:u64)->Self {
        Elf {
            calrories: cal,
        }
    }
}

fn solution() {
    let _input = include_str!("../input.txt");
    let mut tmp_sum: u64 = 0;
    let mut elves = Vec::<Elf>::new();

    for line in _input.lines() {
        if line == "" {
            elves.push(Elf::new(tmp_sum));
            tmp_sum = 0;
            continue;
        }
        tmp_sum += line.parse::<u64>().unwrap();
    }
    elves.sort_by(|a, b| b.cmp(a));
    println!("{}", elves[0].calrories);
    println!("{}", elves[0].calrories + elves[1].calrories + elves[2].calrories);
}
