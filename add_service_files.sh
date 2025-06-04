#!/usr/bin/env bash

ln -fsv "$(realpath systemd_service_files/ddns-updater.service)" /etc/systemd/system/ddns-updater.service
ln -fsv  "$(realpath systemd_service_files/ddns-updater.timer)" /etc/systemd/system/ddns-updater.timer

systemctl enable --now ddns-updater.timer
