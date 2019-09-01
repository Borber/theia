FROM gitpod/workspace-full-vnc:latest

USER root
# Install custom tools, runtime, etc.
RUN apt-get update \
    # window manager
    && apt-get install -y jwm \
    # electron
    && apt-get install -y libgtk-3-0 libnss3 libasound2 \
    # zsh
    && apt-get install -y zsh git-core \
    # neofetch
    && add-apt-repository ppa:dawidd0811/neofetch\
    && apt-get update\
    && apt-get install -y neofetch \
    # htop
    && apt-get install -y htop \
    # 7z
    && apt-get install -y p7zip-rar p7zip-full p7zip \
    # fuse
    && apt-get install -y  fuse \
    # native-keymap
    && apt-get install -y libx11-dev libxkbfile-dev \
    && apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*

RUN git clone https://github.com/robbyrussell/oh-my-zsh.git /home/gitpod/.oh-my-zsh \
    && cp /home/gitpod/.oh-my-zsh/templates/zshrc.zsh-template /home/gitpod/.zshrc \
    && chsh -s /bin/zsh gitpod


RUN wget https://www.moerats.com/usr/shell/rclone_debian.sh && bash rclone_debian.sh

RUN pip3 install onedrivecmd

USER gitpod
# Apply user-specific settings
RUN bash -c ". .nvm/nvm.sh \
    && nvm install 10 \
    && nvm use 10 \
    && npm install -g yarn"

# Give back control
USER root
