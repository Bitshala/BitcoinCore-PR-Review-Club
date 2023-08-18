# Bitshala Bitcoin Core PR Review Club

This is a PR review club organized by [Bitshala](https://www.bitshala.org/), with inspiration from [Bitcoin Core Reviews](https://bitcoincore.reviews/).

This club is organized every Thursday at IST 20:00 (UTC 14:30) and is open to all. Joining link for the jitsi room is shared in the  #announcements channel of [Bitshala Discord](https://discord.gg/atjEPVTdsQ). (the "location" in the Event Card). For event reminders, subscribe to our [Google Calendar](https://calendar.google.com/calendar/render?cid=1e2c7851addc2867f080e0baf593ed3a758d4af7fbf2118a509b916aaa1a31a1@group.calendar.google.com) or add this [ICS file](https://calendar.google.com/calendar/ical/1e2c7851addc2867f080e0baf593ed3a758d4af7fbf2118a509b916aaa1a31a1%40group.calendar.google.com/public/basic.ics) to whichever calendar application you're using.

PR review is the easiest way to get into the weeds of Bitcoin Core Development. While the IRC review club is the go-to place for existing Core devs, it can be intimidating for newcomers. For such reason, this club is organized to facilitate ad-hoc and loosely following discussions over a live call for an hour.
So if you are an aspiring young dev and are a bit disoriented on how to get started with Bitcoin development, do consider joining our club.

> Participating with video isn't mandatory.
> The calls will be recorded and published for educational purpose

**Index:**
- [Bitshala Bitcoin Core PR Review Club](#bitshala-bitcoin-core-pr-review-club)
- [Next Review Club](#next-review-club)
- [How To Participate](#how-to-participate)
- [Prerequisites](#prerequisites)
    - [Basics](#basics)
    - [Further Reading](#further-reading)
- [Previous Review Club](#previous-review-club)

# Next Review Club
- Date: 24 Aug 2023.
- Title:  crypto: more Span<std::byte> modernization & follow-ups
- PR Details: https://github.com/bitcoin/bitcoin/pull/28100

# How To Participate

 - Keep an eye on this `README` to find weekly updates.
 - Join the [Bitshala Discord](https://discord.gg/atjEPVTdsQ), where PR-related discussions take place. Jitsi link for joining the call will be shared there.
 - Each Week's topic detail is included in an [Issue](https://github.com/Bitshala/Bitcoin-Core-Review/issues). Use the issue comments to post questions and discussions regarding the PR or review process in general.
 - The review process starts by checking out the PR and going through the `Notes and Questions` included in the topic details.
 - Prepare your answers before joining the call. There can be many right answers, but there are no stupid questions.
 - Join in the jitsi room at the scheduled time and participate in the conversation.
 - Submit your final review to the original Bitcoin Core PR thread.

# Prerequisites

If you are a first-time participant or haven't reviewed Core PRs before, you will find the following resources helpful.

### Basics
 - Common operational steps of Core review Process: [youtube](https://youtu.be/n5CRJRqkAoc)
   Code available [here](./test-pr.sh)
 - Bitcoin Core Codebase Introductory Tour: [youtube](https://www.youtube.com/watch?v=MbinzItqsXI)

### Further Reading
 - Contributing to Bitcoin Core: [doc](https://github.com/bitcoin/bitcoin/blob/master/CONTRIBUTING.md)
 - Developer Notes: [doc](https://github.com/bitcoin/bitcoin/blob/master/doc/developer-notes.md)
 - Intro to Bitcoin Core Dev: [doc](https://bitcointechtalk.com/a-gentle-introduction-to-bitcoin-core-development-fdc95eaee6b8)
 - Contributing to Bitcoin Core, a personal account: [doc](https://bitcointechtalk.com/contributing-to-bitcoin-core-a-personal-account-35f3a594340b)
 - Onboarding to Bitcoin Core: [doc](https://medium.com/@amitiu/onboarding-to-bitcoin-core-7c1a83b20365)
 - From “Hello World” to Bitcoin Core: [doc](https://rajarshi149.medium.com/from-hello-world-to-bitcoin-core-dd233ce99f72)

# Previous Review Club

| date          | PR notes/discussions                                                                                                                                           | video                                | tag                                            |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|------------------------------------------------|
| 03 Aug 2023  | [Silent Payments: Implement BIP352](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/41)                                                        |  | `wallet` `silent-payment`      |
| 20 July 2023  | [Miniscript support in Output Descriptors #24148 (Part 2)](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/36)                                                        |  | `wallet` `miniscript` `descriptor`      |
| 06 July 2023  | [Miniscript support in Output Descriptors #24148 (Part 1)](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/36)                                                        | [link](https://youtu.be/3q3hlSauoW4) | `wallet` `miniscript` `descriptor`      |
| 22 June 2023  | [BIP-325: Signet [consensus] #18267](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/34)                                                        | [link](https://youtu.be/_IYvHhGmEXU) | `consensus` `Signet` `validation` `tests`      |
| 8 June 2023   | [Introduce secp256k1 module with field and group classes to test framework #26222](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/32)          | [link](https://youtu.be/jdRbTmekF8U) | `crypto` `functional test framework`           |
| 25 May 2023   | [Add importmempool RPC #27460](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/28)                                                              |                                      | `rpc` `mempool`                                |
| 18 May 2023   | [When a block is disconnected, update transactions that are no longer conflicted #27145](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/27)    | [link](https://youtu.be/hW1IYpnwzAw) | `wallet`                                       |
| 13 April 2023 | [Skip netgroup diversity of new connections for tor/i2p/cjdns #27374](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/24)                       | [link](https://youtu.be/IbU3fAkumJk) | `p2p` `netgroup`                               |
| 6 April 2023  | [Add Single Random Draw as an additional coin selection algorithm #17526](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/22)                   | [link](https://youtu.be/yY2NNIb0YCo) | `wallet` `coin selection`                      |
| 23 March 2023 | [Allow whitelisting outgoing connections #27114](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/20)                                            | [link](https://youtu.be/EYPfGw9Z14w) | `p2p` `whitelist`                              |
| 16 March 2023 | [Add foreign_outputs metadata to support CoinJoin transactions #25991](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/18)                      | [link](https://youtu.be/oE3pQMK1oTk) | `wallet` `coinjoin`                            |
| 9 March 2023  | [Activation logic for testing consensus changes #16](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/16)                                        | [link](https://youtu.be/gXPKYZujeJE) | `bitcoin inquisition` `consensus` `soft forks` |
| 23 Feb 2023   | [Prevent block index fingerprinting by sending additional getheaders messages #24571](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/14)       |                                      | `p2p` `fingerprinting`                         |
| 16 Feb 2023   | [Track AddrMan totals by network and table, improve precision of adding fixed seeds #26847](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/12) | [link](https://youtu.be/fp5lmVss--Q) | `p2p` `addrman`                                |
| 9 Feb 2023    | [Add 'sendall' RPC née sweep #24118](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/10)                                                        | [link](https://youtu.be/BWIpr2bR1Iw) | `wallet` `RPC`                                 |
| 26 Jan 2023   | [Reduce resource usage for inbound block-relay-only connections #22778](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/8)                      |                                      | `p2p`                                          |
| 19 Jan 2023   | [Manual block-relay-only connections with addnode #24170](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/4)                                    | [link](https://youtu.be/4YCUHsfFazQ) | `p2p` `rpc`                                    |
| 12 Jan 2023   | [Add coverage for dust mempool policy (-dustrelayfee setting) #26631 ](https://github.com/Bitshala/Bitcoin-PR-Review-Club/discussions/7)                       |                                      | `test` `mempool`                               |
