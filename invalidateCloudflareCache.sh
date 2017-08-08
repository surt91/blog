echo "Clear Cloudflare's cache"

curl -X DELETE "https://api.cloudflare.com/client/v4/zones/4f12df4345095997e5c542b9bd3914d4/purge_cache" \
     -H "Content-Type:application/json" \
     -H "X-Auth-Key:$CLOUDFLARE_TOKEN" \
     -H "X-Auth-Email:$EMAIL" \
     --data '{"purge_everything":true}'
