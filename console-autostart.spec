Name     : console-autostart
Version  : 1
Release  : 3
Summary  : Auto-start the tty1 terminal login
Group    : Default
License  : LGPL-2.1
Requires : systemd-bin

%description
Adds the getty@tty1 unit autostart symlink.

%prep

%build

%install
export SOURCE_DATE_EPOCH=1527111250
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/lib/systemd/system/getty.target.wants/
ln -sf ../getty@.service %{buildroot}/usr/lib/systemd/system/getty.target.wants/getty@tty1.service

%files
%defattr(-,root,root,-)
/usr/lib/systemd/system/getty.target.wants/getty@tty1.service
