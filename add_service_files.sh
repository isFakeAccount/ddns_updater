#!/usr/bin/env bash

mkdir -p ~/.config/systemd/user
ln -fsv "$(realpath systemd_service_files/ddns-updater.service)" ~/.config/systemd/user/ddns-updater.service
ln -fsv  "$(realpath systemd_service_files/ddns-updater.timer)" ~/.config/systemd/user/ddns-updater.timer

systemctl --user enable ddns-updater.service
systemctl --user enable ddns-updater.timer
systemctl --user start ddns-updater.timer
