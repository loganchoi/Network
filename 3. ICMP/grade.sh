#!/bin/bash

######## Variable globals -> ########
# The file containing the "main" entry point for the program.
# In C or C++, this is the file containing the main() function
# In Python, this is whichever file you run via python3 whatever.py
# In Bash, this is whichever file you run via bash whatever.sh
# In Rust, this is src/main.rs
main_file="udp_echo_client_scapy.py"

# Any arguments you want passed to the main driver, upon excution.
# If you do not have any arguments, just leave as an empty string, ""
main_file_arguments=""

# The language that the assignment is written in.  Currently supported
# options are "cpp", "python", "bash", "rust"
language="python"

# Whether or not to score the student using a static analyzer.
# For Python, this is the mypy type-checker.
# For C or C++, this is cppcheck.
# For Bash, this is shellcheck
# Not needed at all with rust?
enable_static_analysis=false

# Whether or not to score the student using an autoformatter (dock points
# if not formatted correctly).
# For Python, this is black.
# For C++, this is clang-format.
# For Bash, this is shfmt
# For Rust, this is rustfmt
enable_format_check=true

# Whether or not to use fuzzy or ridig diffs
# If you choose true, fuzzy diffs will give partial credit.
# This can be helpful for string-heavy assignments,
# where correctness is reasonable to estimate statistically.
# If you choose false, rigid diffs will be all-or-none.
# This is helpful when the assignment is mathy,
# where correctness is not reasonable to estimate statistically.
fuzzy_partial_credit=true

# The timeout duration in seconds for killing a student process.
# This can limit infinite run-times.
# For computationally expensive operations, you may increase this time as desired.
process_timeout=15

# The file to which the final grade is written
# This file can be saved as as artifact in gitlb CI/CD, and used to upload scores to Canvas using assigner.
student_file="results.txt"
######## <- Variable globals ########

######## File and type existence tests -> ########
# Load the specified assosicative array with files you want to check for the existence of.
# Key is the file, and Value must be a sub-string within what is produced by the bash command:
# $ file file.whatever
declare -A file_arr
file_arr=(
    ["iactuallytestedthis-upd_echo_scapy.png"]="PNG image data"
    ["iactuallytestedthis-icmp_ping_scapy.png"]="PNG image data"
    ["report.md"]="ASCII text"
)
######## <- File and type existence tests ########

######## Custom tests -> ########
# Any tests other than the unit tests and the stdout diff tests belong here,
# and must be bash functions whose names begin with "custom_test".
# Custom tests should report their score by assigning their result (0-100)
# to the custom_test_score, e.g.:
# custom_test_score=100
# Custom tests are performed alphabetically,
# so number them if you want them in order.

custom_test_0() {
    custom_test_score=0
    if grep --color=auto -r "import socket" *client_scapy.py; then
        custom_test_score=0
        echo "No using socket, just use scapy!"
        return
    fi
    if grep --color=auto -r "from socket" *client_scapy.py; then
        custom_test_score=0
        echo "No using socket, just use scapy!"
        return
    fi
    if grep --color=auto -r "AF_INET" *client_scapy.py; then
        custom_test_score=0
        echo "No using socket, just use scapy!"
        return
    fi
    custom_test_score=100
}

custom_test_1() {
    custom_test_score=0
    python3 udp_echo_server.py &
    server_PID=$!
    rm custom_tests/outputs/*
    if grep 'docker\|lxc' /proc/1/cgroup >/dev/null 2>&1; then
        python3 udp_echo_client_scapy.py localhost 12000 10 1 >custom_tests/outputs/t1.out
    else
        sudo python3 udp_echo_client_scapy.py localhost 12000 10 1 >custom_tests/outputs/t1.out
    fi
    if ! diff -yZB --width=160 custom_tests/outputs/t1.out custom_tests/goals/t1.out; then
        custom_test_score=0
        kill $server_PID
        return
    fi
    kill $server_PID
    custom_test_score=100
}

custom_test_2() {
    custom_test_score=0
    if grep 'docker\|lxc' /proc/1/cgroup >/dev/null 2>&1; then
        python3 icmp_ping_client_scapy.py localhost 12000 12 2 >custom_tests/outputs/t2.out
    else
        sudo python3 icmp_ping_client_scapy.py localhost 12000 12 2 >custom_tests/outputs/t2.out
    fi
    if ! diff -yZB --width=160 custom_tests/outputs/t2.out custom_tests/goals/t2.out; then
        custom_test_score=0
        return
    fi
    custom_test_score=100
}
######## <- Custom tests ########

source .admin_files/grade_backend.sh
