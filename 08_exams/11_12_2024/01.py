from collections import deque

suggested_links = deque([int(link) for link in input().split(" ")])
featured_articles = [int(a) for a in input().split(" ")]
target_engagement_value = int(input())

final_feed = []

while suggested_links and featured_articles:
    fifo_element = suggested_links.popleft()
    lifo_element = featured_articles.pop()

    if fifo_element > lifo_element:
        greater, smaller, origin = fifo_element, lifo_element, "FIFO"
    elif lifo_element > fifo_element:
        greater, smaller, origin = lifo_element, fifo_element, "LIFO"
    else:
        final_feed.append(0)
        continue

    remainder = greater % smaller

    if origin == "FIFO":
        final_feed.append(-remainder)
    else:
        final_feed.append(remainder)

    if remainder != 0:
        if origin == "FIFO":
            suggested_links.append(remainder * 2)  # Return to the end of FIFO
        else:
            featured_articles.append(remainder * 2)   # Return to the end of LIFO

total_engagement_value = sum(final_feed)

print(f"Final Feed: {', '.join(str(x) for x in  final_feed)}")
if total_engagement_value >= target_engagement_value:
    print(f"Goal achieved! Engagement Value: {total_engagement_value}")
else:
    shortfall = target_engagement_value - total_engagement_value
    print(f"Goal not achieved! Short by: {shortfall}")