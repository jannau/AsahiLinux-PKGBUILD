# Generated by rust2rpm 27
%bcond check 1

# prevent library files from being installed
%global cargo_install_lib 0

%global crate muvm

Name:           rust-muvm
Version:        0.2.0
Release:        %autorelease
Summary:        Run programs from your system in a microVM

License:        MIT
URL:            https://crates.io/crates/muvm
Source:         %{crates_source}
Patch1:         0001-x11-Fix-XAUTHORITY-handling-for-wildcard-DISPLAY.patch

BuildRequires:  cargo-rpm-macros >= 26

# libkrun only supports x86_64 and aarch64
ExclusiveArch:  x86_64 aarch64

%global _description %{expand:
Run programs from your system in a microVM.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
License:        Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND MIT AND (MIT OR Apache-2.0) AND (Unlicense OR MIT)
# LICENSE.dependencies contains a full license breakdown

# This crate was renamed from krun to avoid a conflict with crun-krun. For
# that reason, we only set Obsoletes, not Provides, to avoid perpetuating the
# conflict. This should be removed once f42 is EOL.
Obsoletes:      krun < 0.1.0-2

# dhcpcd support is broken in upstream
# https://github.com/AsahiLinux/muvm/issues/77
Requires:       dhcp-client
Requires:       libkrun >= 1.9.8-1
Requires:       passt
Requires:       socat
Requires:       sommelier

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/muvm
%{_bindir}/muvm-guest
%{_bindir}/muvm-hidpipe
%{_bindir}/muvm-server
%{_bindir}/muvm-x11bridge

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog