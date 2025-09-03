SELECT
  file.version,
  COUNT(*) AS download_count
FROM
  `bigquery-public-data.pypi.file_downloads`
WHERE
  file.project = 'keras'
  AND DATE(timestamp) BETWEEN '2025-03-05' AND '2025-03-26'
GROUP BY
  file.version
ORDER BY
  download_count DESC
