Name: ojuba-fonts
Version: 2.1
Release: 1%{?dist}
Summary: Ojuba Fonts
Source: ojuba-fonts.tar.xz
Summary(ar): خطوط أعجوبة
License: WAQFv2
URL: https://ojuba.org
BuildArch: noarch
Requires: amiri-fonts
Requires: amiri-quran-fonts
Requires: arabeyes-core-fonts
Requires: arabeyes-decorative-fonts
Requires: aref-ruqaa-fonts
Requires: bicon-fonts
Requires: dejavu-sans-fonts
Requires: dejavu-sans-mono-fonts
Requires: dejavu-serif-fonts
Requires: farsi-fonts
Requires: google-droid-sans-fonts
Requires: google-droid-sans-mono-fonts
Requires: google-droid-serif-fonts
Requires: google-noto-kufi-arabic-fonts
Requires: google-noto-naskh-arabic-fonts
Requires: google-noto-naskh-arabic-ui-fonts
Requires: google-noto-sans-fonts
Requires: jameel-noori-nastaleeq-fonts
Requires: jozoor-fonts
Requires: jozoor-flat-fonts
Requires: kacst-art-fonts
Requires: kacst-book-fonts
Requires: kacst-decorative-fonts
Requires: kacst-digital-fonts
Requires: kacst-farsi-fonts
Requires: kacst-letter-fonts
Requires: kacst-naskh-fonts
Requires: kacst-office-fonts
Requires: kacst-one-fonts
Requires: kacst-pen-fonts
Requires: kacst-poster-fonts
Requires: kacst-qurn-fonts
Requires: kacst-screen-fonts
Requires: kacst-title-fonts
Requires: kacst-titlel-fonts
Requires: kfgqpc-fonts
Requires: kfgqpc-hafs-fonts
Requires: layla-arcyarc-fonts
Requires: layla-basic-arabic-fonts
Requires: layla-boxer-fonts
Requires: layla-digital-fonts
Requires: layla-diwani-fonts
Requires: layla-koufi-fonts
Requires: layla-ruqaa-fonts
Requires: layla-thuluth-fonts
Requires: mada-fonts
Requires: naqsh-fonts
Requires: reem-kufi-fonts

%prep
#%autosetup -n %{name}

%install
#install -m 0755 -d %{buildroot}%{_sysconfdir}/fonts/{conf.d,conf.avail}
#install -m 0644 conf.d/* %{buildroot}%{_sysconfdir}/fonts/conf.d
#install -m 0644 conf.avail/* %{buildroot}%{_sysconfdir}/fonts/conf.avail


# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2017 Mosaab Alzoubi <moceap@hotmail.com> -->
<!--
EmailAddress: moceap@hotmail.com
SentUpstream: 2017-1-9
-->
<application>
  <id type="desktop">ojuba-fonts.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Ojuba Fonts</summary>
  <summary xml:lang="ar">خطوط أعجوبة</summary>
  <description>
    <p>
      Ojuba fonts META package of the Best Arabic freesoftware fonts.
    </p>
  </description>
  <description xml:lang="ar">
    <p>
     تجميعة أعجوبة لأفضل الخطوط العربية الحرة.
    </p>
  </description>
  <url type="homepage">http://ojuba.org</url>
  <screenshots>
    <screenshot type="default">http://ojuba.org/screenshots/%{name}.png</screenshot>
  </screenshots>
  <updatecontact>moceap@hotmail.com</updatecontact>
</application>
EOF


#Create desktop file
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Type=Application
Name=Ojuba Fonts
Name[ar]=خطوط أعجوبة
Exec=echo "Ojuba Fonts %{version}"
NoDisplay=true
X-Desktop-File-Install-Version=0.23
EOF


%description
Ojuba fonts META package of the Best Arabic freesoftware fonts.

%description -l ar
تجميعة أعجوبة لأفضل الخطوط العربية الحرة.

%post
fc-cache -fv

%postun
fc-cache -fv

%files
#%{_sysconfdir}/fonts/conf.d/*
#%{_sysconfdir}/fonts/conf.avail/*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop

%changelog
* Mon Oct 24 2022 Mosaab Alzoubi <moceap[AT]fedoraproject[DOT]org> - 2.1-1
- Stop custom configuration till review

* Wed Oct 19 2022 Mosaab Alzoubi <moceap[AT]fedoraproject[DOT]org> - 2-1
- Update to ver 2
- Add layla-arcyarc-fonts
- Remove google-droid-kufi-fonts moved to google-droid-sans-fonts
- Remove google-noto-mono-fonts obsoleted by Google Noto Sans Mono

* Sat Feb 25 2017 Mosaab Alzoubi <moceap@hotmail.com> - 1-6
- Add fonts

* Thu Feb 23 2017 Mosaab Alzoubi <moceap@hotmail.com> - 1-5
- Add Ojuba font settings

* Mon Jan 9 2017 Mosaab Alzoubi <moceap@hotmail.com> - 1-4
- Add Fonts
- Fix appdata by adding desktop file

* Wed Jan 4 2017 Mosaab Alzoubi <moceap@hotmail.com> - 1-3
- Add Fonts

* Sat Dec 31 2016 Mosaab Alzoubi <moceap@hotmail.com> - 1-2
- Add appdata

* Sat Dec 31 2016 Mosaab Alzoubi <moceap@hotmail.com> - 1-1
- Initial
