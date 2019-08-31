wget https://www.moerats.com/usr/shell/rclone_debian.sh && bash rclone_debian.sh
rclone config
mkdir /workspace/ONE
rclone mount BORBER_ONE:BORBER /workspace/ONE --copy-links --no-gzip-encoding --no-check-certificate --allow-other --allow-non-empty --umask 000
