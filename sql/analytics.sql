SELECT userId, COUNT(*) AS post_count
FROM posts
GROUP BY userId
ORDER BY post_count DESC;