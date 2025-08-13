#!/bin/sh

file="/mnt/onboard/.kobo/Kobo/Kobo eReader.conf"

locale="vi"
searchstr="ExtraLocales="
section="ApplicationPreferences"

ret=`grep $searchstr "$file" | sed 's/^.*=//'`
if [ -z "$ret" ]; then
    sed -i "/\[$section\]/a $searchstr$locale" "$file"
else
    if [ "${ret#*$locale}" = "$ret" ]; then
        sed -i "s/\($searchstr.*\)/\1, $locale/" "$file"
    fi
fi

curlocale="vi"
searchstr="CurrentLocale="
section="ApplicationPreferences"

ret=`grep $section "$file"`
if [ -z "$ret" ]; then
    echo "" >> "$file"
    echo "[$section]" >> "$file"
fi

ret=`grep $searchstr "$file" | sed 's/^.*=//'`

if [ -z "$ret" ]; then
    sed -i "/\[$section\]/a $searchstr$curlocale" "$file"
else
    if [ "${ret%$curlocale}" = "$ret" ]; then
        sed -i "s/\($searchstr\)\(.*\)/\1$curlocale/" "$file"
    fi
fi


rm /etc/udev/rules.d/update_conf.rules
rm /root/update_conf.sh
