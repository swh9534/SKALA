#!/bin/sh

# 파일 경로 설정
FILE="/app/my-info.txt"

echo "Container is now waiting... Press Ctrl+C to stop."
# 파일 내용 출력
echo ""
echo ""
echo ""
cat "$FILE"

# 무한 대기 상태로 유지
tail -f /dev/null

