Summary: Linux wireless regulatory database
Name: wireless-regdb
Version: 2009.01.15
Release: 1
License: ISC
Group: System Enviroment/Base
Source: http://wireless.kernel.org/download/wireless-regdb/wireless-regdb-2009-01-15.tar.bz2
URL: http://wireless.kernel.org/en/developers/Regulatory/
Packager: Luis R. Rodriguez <mcgrof@gmail.com>
BuildRoot : /var/tmp/%{name}-buildroot
Requires: python
BuildArch: noarch

%define crda_lib /usr/lib/crda
%define crda_key_path /etc/wireless-regdb/pubkeys/

%description
This package contains the wireless regulatory database used by all
cfg80211 based Linux wireless drivers. The wireless database being
used is maintained by John Linville, the Linux wireless kernel maintainer
http://wireless.kernel.org/en/developers/Regulatory/

%prep
%setup -n %name-2009-01-15
%build
%install
install -m 755 -d %buildroot/%crda_lib
install -m 755 -d %buildroot/%crda_key_path
install -m 644 regulatory.bin %buildroot/%{crda_lib}/regulatory.bin
install -m 644 linville.key.pub.pem %buildroot/%{crda_key_path}/linville.key.pub.pem
%files
%crda_lib/regulatory.bin
%crda_key_path/linville.key.pub.pem
%doc README LICENSE

%changelog
* Wed Feb 03 2010 - mcgrof@gmail.com
- Added new CRDA key path: /etc/wireless-regdb/pubkeys/ for use when
  CRDA >= 1.1.1 and when openssl is used
* Fri Jan 23 2009 - mcgrof@gmail.com
- Started wireless-regdb package

