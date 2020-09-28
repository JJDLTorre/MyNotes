sed -ie 's/^.*: history-search-backward/\"\\e[A\": history-search-backward/' /etc/inputrc
sed -ie 's/^.*: history-search-forward/\"\\e[B\": history-search-forward/' /etc/inputrc