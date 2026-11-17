# Mission 7 — How computers communicate

## 1. Task / objective

Explain networking terms, check a public website and look up its domain from Terminal.

## 2. Work completed

### Task 7.1 — Network concepts

| Concept | Explanation | Example |
| --- | --- | --- |
| LAN | Links devices in a small area, such as a room or building. | A laptop and printer on the same home network. |
| MAN | Links networks across a city or metropolitan area. | A city fibre network connecting public library branches. |
| WAN | Links far-apart networks across regions or countries. | A network connecting offices in Bengaluru and Delhi. |
| DNS | Looks up domain records, including IP addresses used to reach a site. | Looking up the A records for example.com. |
| Router | Forwards packets from one network toward another. | A home router forwards a laptop’s traffic toward the internet provider. |
| Protocol | Defines how devices format and exchange messages. | HTTP defines requests and responses for web resources. |
| Packet switching | Sends small units of data through shared network links. | A web response is transported in packets that can be reassembled at the destination. |
| Client–server | A client requests a service and a server provides a response. | A browser requests a page and a web server sends it. |

### Task 7.2 — Network observations

`curl -fsSI --max-time 12 https://example.com/` received `HTTP/2 200`. The HTTPS connectivity check shows the machine could reach the service and receive a successful response to a headers request. `dig -4 +short example.com A` returned the public IPv4 answers `172.66.147.243` and `104.20.23.154` at the time of testing. A DNS lookup displays records for the domain. With an A lookup, the answers are IPv4 addresses. Browsers can use a DNS result or a cached result to find the address for the requested name.

### Task 7.3 — What happens when you open a website?

1. The browser, acting as the **client**, reads the URL and identifies the hostname and resource path.
2. It uses a cached address or asks **DNS** to resolve the hostname.
3. Packets travel over the local network through its router and across other networks toward the destination.
4. The client establishes an encrypted connection for HTTPS and sends a request using the HTTP **protocol**.
5. The web **server** receives the request and sends a response with a status, headers and usually the requested content.
6. The browser reads the response, requests any additional resources and renders the page for the user.

## 3. Commands / tools used

`curl -fsSI` requested only the public site’s headers. `dig -4 +short example.com A` queried public IPv4 address records and printed a short answer.

## 4. My understanding

DNS supplies an address associated with a name. Routers move packets toward that address, and HTTP gives the browser and web server rules for their request and response.

## 5. Difficulties faced

The initial shell session restricted network access.

## 6. How I resolved them

A separately approved read-only check successfully reached the example website and looked up its public domain.

## 7. Evidence / files

The selected HTTP status and public DNS answers are shown above.

## 8. Commit details

Commit message: `Explain networking concepts and website communication`. The [public main-branch history](https://github.com/MassGethu/digital-detective-8060/commits/main/) shows the mission commits.
