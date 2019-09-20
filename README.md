# Spotify Album Liker

Miss the old Spotify UI in which you could see all of your songs in a single location? Want to listen to all songs of your liked albums alongside your individually liked songs? This script is for you!

After the recent updates to the Spotify UI, many users find the new layout annoying

Some examples of complaints:
 - https://community.spotify.com/t5/Android/quot-Liked-songs-quot-playlist-doesn-t-contain-all-my-liked/td-p/4749441
 - https://community.spotify.com/t5/Android/New-Liked-Songs-and-Saved-Albums-problem/td-p/4699202
 - https://community.spotify.com/t5/iOS-iPhone-iPad/quot-Liked-Songs-quot-Playlist-automatically-updated-with-songs/td-p/4771077
 
 Authorizing, and running this script will identify all songs from your liked albums, and like those songs as well. This process allows you to listen and see all of your songs together in the "Liked Songs" section as you were previously able to before the UI update.
 
 Note: This script does not automatically add future liked albums to the songs list. Though, you can run it as much as you'd like (daily, weekly, etc) with no problems, or duplicate songs
 
 ## Setup and Running
Setup authorization for your Spotify profile by following: https://developer.spotify.com/documentation/general/guides/app-settings/#register-your-app
Be sure to make note of the client_id, client_secret, and redirect_url you use

Install this script with pip

```bash
pip install spotify-albumliker
```
Then, run the cli utility and provide your authorization information
```bash
spoifyliker myusername123 --client_id <client-id> --client_secret <client-secret> --redirect_uri <uri>
```
Follow the prompts to authorize the script, once completed, all songs will be available in your songs list

## Further improvements
As it is today, this script will add all songs from your saved albums at the time of the run, but it will not remove songs from albums you no longer have saved. If there is interest, and Spotify doesn't fix this issue I will add the feature to further synchronize songs and remove any songs from albums you no longer like
