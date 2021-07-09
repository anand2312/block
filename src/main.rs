use regex::Regex;
use structopt::StructOpt;


#[derive(StructOpt)]
#[structopt(name = "Block", about = "Block distracting websites.")]
struct Block {
    /// URLs to block
    #[structopt(use_delimiter = true, value_delimiter = " ")]
    sites: Vec<String>,
    /// Time to block for
    time: String
}

/// Struct representing the time for which a website should be blocked
struct BlockTime {
    hrs: usize,
    mins: usize,
    sec: usize,
}


impl BlockTime {
    /// Parse an input timestring into an instance of the BlockTime struct
    fn parse_timestring(raw: String) -> BlockTime {
        let re = Regex::new(r"/(?P<hrs>[0-9]*h)(?P<mins>[0-9]*m)(?P<sec>[0-9]*s)").unwrap();
        let captures = re.captures(raw.as_str()).unwrap();

        BlockTime {
            hrs: captures.name("hrs").unwrap().as_str().parse::<usize>().unwrap(),
            mins: captures.name("mins").unwrap().as_str().parse::<usize>().unwrap(),
            sec: captures.name("sec").unwrap().as_str().parse::<usize>().unwrap()
        }
    }
}


fn main () {
    println!("Hello world");
}
