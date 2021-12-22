pub fn day16() {
    fn hex_char_to_binary(hex: char) -> String {
        format!("{:04b}", hex.to_digit(16).unwrap())
    }

    let input: String = std::fs::read_to_string("input/input16.txt")
        .unwrap()
        .chars()
        .map(|ch| hex_char_to_binary(ch))   // input is binary string now!
        .collect();

    day16_part1(input.clone());
    day16_part2(input.clone());
}

fn day16_part1(input: String) {
    fn parse_and_get_version_sum(packet: &str, cursor: &mut usize) -> usize {        // literally, parse string and returns version sum
        let packet_version = binary_str_to_usize(&packet[*cursor..*cursor + 3]); *cursor += 3;      // label V
        let packet_type = binary_str_to_usize(&packet[*cursor..*cursor + 3]); *cursor += 3;         // label T

        let mut subpacket_version_sum = 0;

        if packet_type == 4 {
            while binary_str_to_usize(&packet[*cursor..*cursor + 5]) >= 16 {    // while leading five bits start with 1
                *cursor += 5;
            }
            *cursor += 5;
        } else {
            let length_type_id = binary_str_to_usize(&packet[*cursor..*cursor + 1]); *cursor += 1;  // label I

            if length_type_id == 0 {
                let length_of_subpacket = binary_str_to_usize(&packet[*cursor..*cursor + 15]); *cursor += 15;    // label L
                let finished_cursor = *cursor + length_of_subpacket;

                while *cursor < finished_cursor {
                    subpacket_version_sum += parse_and_get_version_sum(packet, cursor);
                }
            } else {
                let number_of_subpacket = binary_str_to_usize(&packet[*cursor..*cursor + 11]); *cursor += 11;   // label L
                
                for _ in 0..number_of_subpacket {
                    subpacket_version_sum += parse_and_get_version_sum(packet, cursor);
                }
            }
        }

        packet_version + subpacket_version_sum
    }

    let version_sum = parse_and_get_version_sum(&input, &mut 0);

    println!("Part One: {}", version_sum);
}

fn day16_part2(input: String) {
    fn parse_and_get_value(packet: &str, cursor: &mut usize) -> usize {
        let _packet_version = binary_str_to_usize(&packet[*cursor..*cursor + 3]); *cursor += 3;      // label V
        let packet_type = binary_str_to_usize(&packet[*cursor..*cursor + 3]); *cursor += 3;         // label T

        let mut value = 0;

        if packet_type == 4 {   // literal values: the only case which does not have subpacket
            while binary_str_to_usize(&packet[*cursor..*cursor + 5]) >= 16 {    // while leading five bits start with 1
                value += binary_str_to_usize(&packet[*cursor + 1..*cursor + 5]);
                value *= 16;
                *cursor += 5;
            }
            value += binary_str_to_usize(&packet[*cursor + 1..*cursor + 5]);
            *cursor += 5;
        } else {
            let mut subpacket_value: Vec<usize> = vec![];

            let length_type_id = binary_str_to_usize(&packet[*cursor..*cursor + 1]); *cursor += 1;  // label I

            if length_type_id == 0 {
                let length_of_subpacket = binary_str_to_usize(&packet[*cursor..*cursor + 15]); *cursor += 15;    // label L
                let finished_cursor = *cursor + length_of_subpacket;

                while *cursor < finished_cursor {
                    subpacket_value.push(parse_and_get_value(packet, cursor));
                }
            } else {
                let number_of_subpacket = binary_str_to_usize(&packet[*cursor..*cursor + 11]); *cursor += 11;   // label L
                
                for _ in 0..number_of_subpacket {
                    subpacket_value.push(parse_and_get_value(packet, cursor));
                }
            }

            value = match packet_type {
                0 => subpacket_value.iter().sum(),
                1 => subpacket_value.iter().product(),
                2 => *subpacket_value.iter().min().unwrap(),
                3 => *subpacket_value.iter().max().unwrap(),
                5 => if subpacket_value[0] > subpacket_value[1] { 1 } else { 0 },
                6 => if subpacket_value[0] < subpacket_value[1] { 1 } else { 0 },
                7 => if subpacket_value[0] == subpacket_value[1] { 1 } else { 0 },
                _ => 0
            }
        }

        value
    }

    let value = parse_and_get_value(&input, &mut 0);
    
    println!("Part Two: {}", value);
}

fn binary_str_to_usize(binary: &str) -> usize {
    usize::from_str_radix(binary, 2).unwrap()
}