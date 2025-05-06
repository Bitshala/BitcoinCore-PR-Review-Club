# Bitshala Bitcoin Core PR Review Club

This is a PR review club organized by [Bitshala](https://www.bitshala.org/), with inspiration from [Bitcoin Core Reviews](https://bitcoincore.reviews/).

## About the Club

This club meets biweekly on Thursdays at IST 19:00 (UTC 13:30) and is open to all. Our mission is to make Bitcoin Core development more accessible to newcomers by providing a supportive environment for PR reviews and discussions.

- **Joining link**: Shared in the #announcements channel of [Bitshala Discord](https://discord.gg/atjEPVTdsQ)
- **Calendar**: Subscribe to our [Google Calendar](https://calendar.google.com/calendar/render?cid=1e2c7851addc2867f080e0baf593ed3a758d4af7fbf2118a509b916aaa1a31a1@group.calendar.google.com) or add this [ICS file](https://calendar.google.com/calendar/ical/1e2c7851addc2867f080e0baf593ed3a758d4af7fbf2118a509b916aaa1a31a1%40group.calendar.google.com/public/basic.ics) to your calendar application

> Participating with video isn't mandatory.
> The calls are recorded and published for educational purposes.

## Table of Contents
- [Next Review Club](#next-review-club)
- [How To Participate](#how-to-participate)
- [Request a PR Review](#request-a-pr-review)
- [Prerequisites](#prerequisites)
    - [Basics](#basics)
    - [Further Reading](#further-reading)
- [Previous Review Club Sessions](#previous-review-club-sessions)

## Next Review Club
- Date: May 16, 2025
- Title: TBA
- PR Details: TBA

## How To Participate

1. Keep an eye on this `README` for weekly updates
2. Join the [Bitshala Discord](https://discord.gg/atjEPVTdsQ), where PR-related discussions take place and meeting links are shared
3. Each review topic is detailed in an [Issue](https://github.com/Bitshala/Bitcoin-Core-Review/issues) - use the comments to post questions and discuss the PR
4. Review process:
   - Check out the PR
   - Go through the "Notes and Questions" in the topic details
   - Prepare your answers before joining the call
   - Join the Jitsi room at the scheduled time
   - Submit your final review to the original Bitcoin Core PR thread

## Request a PR Review

If you'd like to have your Bitcoin Core PR reviewed in our club:

1. Create an [issue](https://github.com/Bitshala/Bitcoin-Core-Review/issues/new) with the following information:
   - Title: "PR Review Request: [Your PR Title]"
   - PR Link: Link to your Bitcoin Core PR
   - Brief description of what your PR does
   - Areas of feedback you're looking for
   - Any specific questions you have about your implementation

2. Bitshala team will review your request and schedule it for an upcoming review session if appropriate

3. You're encouraged to attend the session when your PR is reviewed to provide context and answer questions

## Prerequisites

If you're a first-time participant or haven't reviewed Core PRs before, you'll find these resources helpful:

### Basics
- Common operational steps of Core review Process: [YouTube](https://youtu.be/n5CRJRqkAoc)
  Code available [here](./test-pr.sh)
- Bitcoin Core Codebase Introductory Tour: [YouTube](https://www.youtube.com/watch?v=MbinzItqsXI)

### Further Reading
- Contributing to Bitcoin Core: [doc](https://github.com/bitcoin/bitcoin/blob/master/CONTRIBUTING.md)
- Developer Notes: [doc](https://github.com/bitcoin/bitcoin/blob/master/doc/developer-notes.md)
- Intro to Bitcoin Core Dev: [doc](https://bitcointechtalk.com/a-gentle-introduction-to-bitcoin-core-development-fdc95eaee6b8)
- Contributing to Bitcoin Core, a personal account: [doc](https://johnnewbery.com/contributing-to-bitcoin-core-a-personal-account/)
- Onboarding to Bitcoin Core: [doc](https://medium.com/@amitiu/onboarding-to-bitcoin-core-7c1a83b20365)
- From "Hello World" to Bitcoin Core: [doc](https://rajarshi149.medium.com/from-hello-world-to-bitcoin-core-dd233ce99f72)


# Previous Review Club

| index | date          | PR notes/discussions                                                                                                                                           | video                                                    | tag                                            |
|-------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|------------------------------------------------|
| 54 | 24 Apr 2025 | [Bitcoin-Core v29.0](https://github.com/Bitshala/BitcoinCore-PR-Review-Club/discussions/118) | [link](https://youtu.be/l0FH3OljXgE?si=je9UjR_VpWRZnzDL) | `release` `testing` |
| 53    | 10 Apr 2025 | [Clang/LLVM based coverage generation](https://github.com/Bitshala/BitcoinCore-PR-Review-Club/discussions/109) | [link](https://youtu.be/vmub9voeNMM?si=Brmq0qWxjcmQOnku) | `build` |
| 52    | 13 Mar 2025 | [fuzz: split coinselection harness](https://github.com/Bitshala/BitcoinCore-PR-Review-Club/discussions/107) |  | `fuzz` `tests` |
| 51    | 27 Feb 2025 | [psbt add non-default sighash types to PSBTs and unify sighash type match checking](https://github.com/Bitshala/BitcoinCore-PR-Review-Club/discussions/105) | [link](https://youtu.be/vFiwdDfmcLc?si=VZJ5ZiWaWe3L_f8x) | `p2p` `tests` |
| 50    | 30 Jan 2025 | [test, Call generate RPCs through test framework only, qa: Improve framework.generate* enforcement (#31403 follow-up)](https://github.com/Bitshala/BitcoinCore-PR-Review-Club/discussions/101) | [link](https://youtu.be/aIDZmIV3_ik?si=ifP5b9QgHz8kmBjh) | `rpc` `tests` |
| 49    | 16 Jan 2025 | [add missing segwitv1 test cases to script_standard_tests and exploring v3 transaction relay](https://github.com/Bitshala/BitcoinCore-PR-Review-Club/discussions/99) | [link](https://youtu.be/xdepfElIWqY?si=n4wJ-4mtldu7KgoP) | `p2p` `rbf` |
| 48    | 1 Jan 2025 | [fuzz: Abort if system time is called without mock time being set](https://github.com/Bitshala/BitcoinCore-PR-Review-Club/discussions/97) | [link](https://youtu.be/Qb8pt5q2BYg?si=iOYgQlyEkMNSOPaR) | `fuzz` `tests` |
| 47    | 19 Dec 2025 | [Execute Discover() when bind=0.0.0.0 or :: is set](https://github.com/Bitshala/BitcoinCore-PR-Review-Club/discussions/95) | [link](https://youtu.be/e-3C1vMyXow?si=EyEGnagw5Y6GikSD) | `p2p` `tests` |
| 46    | 5 Dec 2024 | [handle invalid -rpcbind port](https://github.com/Bitshala/BitcoinCore-PR-Review-Club/discussions/110) | [link](https://youtu.be/rlx5BM9iarU?si=K5Ogh_rZbF-nTpcF) | `rpc` `p2p` |
| 45    | 26 Nov 2024 | [(test) clarify timewarp grace period griefing attack](https://github.com/Bitshala/BitcoinCore-PR-Review-Club/discussions/103) |  | `rpc` `p2p` |
| 44    | 21 Nov 2024 | [Settxfeerate](https://github.com/Bitshala/BitcoinCore-PR-Review-Club/discussions/92) | [link](https://youtu.be/IGjSnApE7Vc?si=x60rhdNHZVQaNjBg) | `rpc` `wallet` |
| 43    | 7 Nov 2024 | [Review Club: Drop miniupnp dependency](https://github.com/Bitshala/BitcoinCore-PR-Review-Club/discussions/90) | [link](https://youtu.be/s6QLJq-Dbfs?si=X-u2kDUEIUiUYWnr) | `p2p` `rpc` |
| 42    | 24 Oct 2024 | [Prevention of Stalling when close to the tip](https://github.com/Bitshala/BitcoinCore-PR-Review-Club/discussions/88) | [link](https://youtu.be/qMu_vipflxQ?si=sdQhp91Ttx3J_3MX) | `p2p` |
| 41    | 10 Oct 2024 | [P2P - Increase tx relay rate ](https://github.com/Bitshala/BitcoinCore-PR-Review-Club/discussions/86) |  | `p2p` |
| 40    | 26 Sept 2024 | [Review Club : PSBT input utxo population](https://github.com/Bitshala/BitcoinCore-PR-Review-Club/discussions/111) | [link](https://youtu.be/YCgE339NFAA?si=Lcpi9ulCTICPHLqQ) | `p2p` `rpc` |
| 39    | 19 Sept 2024 | [Review Club: p2p - Tracing in Bitcoin Core](https://github.com/Bitshala/BitcoinCore-PR-Review-Club/discussions/112) |  | `p2p` `tracing` |
| 38    | 5 Sept 2024 | [rpc: Add test-only RPCs under -test=<option> flag ](https://github.com/Bitshala/BitcoinCore-PR-Review-Club/discussions/83) |  | `p2p` |
| 37    | 22 Aug 2024 | [p2p: Increase inbound capacity for block-relay only connections](https://github.com/Bitshala/BitcoinCore-PR-Review-Club/discussions/82) | [link](https://youtu.be/vEdMD6kfRHQ?si=T8zJq5Litob28awM) | `p2p` |
| 36    | 8 Aug 2024 | [RPC : Fix -norpcwhitelist, -norpcallowip, and similar corner case behavior Aug 8 2024](https://github.com/Bitshala/BitcoinCore-PR-Review-Club/discussions/113) | [link](https://youtu.be/dD8AvWereWw?si=_xOrY2wBA5BQgB4i) | `rpc` |
| 35    | 25 July 2024  | [consensus: Store transaction nVersion as uint32_t #29325](https://github.com/Bitshala/BitcoinCore-PR-Review-Club/discussions/72)                              |                                                          | `consensus`                                    |
| 34    | 11 July 2024  | [[Part 3/3: Writing unit tests and fuzz tests] p2p - Fill reconciliation sets](https://github.com/Bitshala/BitcoinCore-PR-Review-Club/discussions/70)          |                                                          | `BIP330` `erlay`                               |                                                                                                                              
| 33    | 13 June 2024  | [[Part 2/3] p2p: Fill reconciliation sets (Erlay) attempt 2 #30116](https://github.com/Bitshala/BitcoinCore-PR-Review-Club/discussions/69)                     |                                                          | `BIP330` `erlay`                               |
| 32    | 23 May 2024   | [[Part 1/3: Introduction] p2p: Fill reconciliation sets (Erlay) attempt 2 #30116](https://github.com/Bitshala/BitcoinCore-PR-Review-Club/discussions/68)       | [link](https://youtu.be/LKMnKYk4x1A)                     | `BIP330` `erlay`                               |
| 31    | 25 April 2024 | [BIP 330 review](https://github.com/Bitshala/BitcoinCore-PR-Review-Club/discussions/67)                                                                        |                                                          | `BIP330` `erlay`                               |
| 30    | 11 April 2024 | [test: refactor: introduce and use calculate_input_weight helper #29777](https://github.com/Bitshala/BitcoinCore-PR-Review-Club/discussions/66)                |                                                          | `test` `refactor`                              |
| 29    | 28 March 2024 | [v27.0 testing](https://github.com/Bitshala/BitcoinCore-PR-Review-Club/discussions/65)                                                                         |                                                          | `testing guide`                                |
| 28    | 14 March 2024 | [follow up ideas for p2p: Allow whitelisting manual connections #27114](https://github.com/bitcoin/bitcoin/pull/27114)                                         |                                                          | `p2p` `net` `whitelist`                        |
| 27    | 22 Feb 2024   | [follow up ideas for test: Fix SegwitV0SignatureMsg nLockTime signedness #29400](https://github.com/bitcoin/bitcoin/pull/29400#discussion_r1481330149)         |                                                          | `good first issue` `test` `locktime`           |
| 26    | 8 Feb 2024    | [rpc: parse legacy pubkeys consistently with specific error messages #28336](https://github.com/Bitshala/BitcoinCore-PR-Review-Club/issues/49)                 |                                                          | `test` `rpc`                                   |
| 25    | 25 Jan 2024   | [test: p2p: check disconnect due to lack of desirable service flags #29279](https://github.com/Bitshala/BitcoinCore-PR-Review-Club/issues/49)                  |                                                          | `test` `p2p`                                   |
| 24    | 4 Jan 2024    | [test: Use test framework utils in functional tests #28528](https://github.com/Bitshala/BitcoinCore-PR-Review-Club/issues/49)                                  | [link](https://youtu.be/Rn2NS4w-Iy4?si=E-xAoZfBU5zxkBib) | `test` `util`                                  |
| 23    | 21 Dec 2023   | [refactor: share and use GenerateRandomKey helper #28455 ](https://github.com/Bitshala/BitcoinCore-PR-Review-Club/issues/49)                                   | [link](https://youtu.be/oro1lM7B6hM?si=VcOYHA6ds7s_Zaoy) | `test` `refactor`                              |
| 22    | 07 Dec 2023   | [[Part 2/2] Functional tests for v2 P2P encryption #24748](https://github.com/Bitshala/BitcoinCore-PR-Review-Club/discussions/50)                              | [link](https://youtu.be/PTkJTYIK3Bc?si=MR22NfUo6sSJPEzb) | `test` `p2p`                                   |
| 21    | 16 Nov 2023   | [[Part 1/2: Introduction] Functional tests for v2 P2P encryption #24748](https://github.com/Bitshala/BitcoinCore-PR-Review-Club/discussions/47)                | [link](https://www.youtube.com/watch?v=5_LZUt1eQaM)      | `test` `p2p`                                   |
| 20    | 07 Sep 2023   | [net: transport abstraction](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/45)                                                                | [link](https://youtu.be/H_nQVD5p-UU?si=rSHfrS0pxHM2xMKa) | `p2p`                                          |
| 19    | 24 Aug 2023   | [crypto: more Span\<std::byte> modernization & follow-ups](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/43)                                  | [link](https://youtu.be/Pb-IPHv3lCg?si=gj5vPqfdQ5AbtzHc) | `crypto` `modern c++`                          |
| 18    | 03 Aug 2023   | [Silent Payments: Implement BIP352](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/41)                                                         |                                                          | `wallet` `silent-payment`                      |
| 17    | 20 July 2023  | [Miniscript support in Output Descriptors #24148 (Part 2)](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/36)                                  | [link](https://youtu.be/WRvhLYLZ_Rw?si=paFQfY7CHsVoTvWU) | `wallet` `miniscript` `descriptor`             |
| 16    | 06 July 2023  | [Miniscript support in Output Descriptors #24148 (Part 1)](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/36)                                  | [link](https://youtu.be/3q3hlSauoW4)                     | `wallet` `miniscript` `descriptor`             |
| 15    | 22 June 2023  | [BIP-325: Signet [consensus] #18267](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/34)                                                        | [link](https://youtu.be/_IYvHhGmEXU)                     | `consensus` `Signet` `validation` `tests`      |
| 14    | 8 June 2023   | [Introduce secp256k1 module with field and group classes to test framework #26222](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/32)          | [link](https://youtu.be/jdRbTmekF8U)                     | `crypto` `functional test framework`           |
| 13    | 25 May 2023   | [Add importmempool RPC #27460](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/28)                                                              |                                                          | `rpc` `mempool`                                |
| 12    | 18 May 2023   | [When a block is disconnected, update transactions that are no longer conflicted #27145](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/27)    | [link](https://youtu.be/hW1IYpnwzAw)                     | `wallet`                                       |
| 11    | 13 April 2023 | [Skip netgroup diversity of new connections for tor/i2p/cjdns #27374](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/24)                       | [link](https://youtu.be/IbU3fAkumJk)                     | `p2p` `netgroup`                               |
| 10    | 6 April 2023  | [Add Single Random Draw as an additional coin selection algorithm #17526](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/22)                   | [link](https://youtu.be/yY2NNIb0YCo)                     | `wallet` `coin selection`                      |
| 9     | 23 March 2023 | [Allow whitelisting outgoing connections #27114](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/20)                                            | [link](https://youtu.be/EYPfGw9Z14w)                     | `p2p` `whitelist`                              |
| 8     | 16 March 2023 | [Add foreign_outputs metadata to support CoinJoin transactions #25991](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/18)                      | [link](https://youtu.be/oE3pQMK1oTk)                     | `wallet` `coinjoin`                            |
| 7     | 9 March 2023  | [Activation logic for testing consensus changes #16](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/16)                                        | [link](https://youtu.be/gXPKYZujeJE)                     | `bitcoin inquisition` `consensus` `soft forks` |
| 6     | 23 Feb 2023   | [Prevent block index fingerprinting by sending additional getheaders messages #24571](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/14)       |                                                          | `p2p` `fingerprinting`                         |
| 5     | 16 Feb 2023   | [Track AddrMan totals by network and table, improve precision of adding fixed seeds #26847](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/12) | [link](https://youtu.be/fp5lmVss--Q)                     | `p2p` `addrman`                                |
| 4     | 9 Feb 2023    | [Add 'sendall' RPC née sweep #24118](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/10)                                                        | [link](https://youtu.be/BWIpr2bR1Iw)                     | `wallet` `RPC`                                 |
| 3     | 26 Jan 2023   | [Reduce resource usage for inbound block-relay-only connections #22778](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/8)                      |                                                          | `p2p`                                          |
| 2     | 19 Jan 2023   | [Manual block-relay-only connections with addnode #24170](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/4)                                    | [link](https://youtu.be/4YCUHsfFazQ)                     | `p2p` `rpc`                                    |
| 1     | 12 Jan 2023   | [Add coverage for dust mempool policy (-dustrelayfee setting) #26631 ](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/7)                       |                                                          | `test` `mempool`                               |
