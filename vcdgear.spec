Summary:	Convert various MPEG file format
Summary(pl.UTF-8):	Konwerter różnego rodzaju plików MPEG
Name:		vcdgear
Version:	1.76
Release:	1
License:	unknown
Group:		Applications/File
Source0:	http://www.vcdgear.com/files/vcdgear176-040415_linux.tar.gz
# Source0-md5:	d5341a6f72122ea73b2be9e44bc14e5d
URL:		http://www.vcdgear.com/
Vendor:		Dracore <dracore@home.com>
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86}

%description
This program allow convert MPEG files in various format:
.cue --> .raw (.cue to .raw/.bin track image), .cue --> .dat,
.cue --> .mpg, .raw --> .dat (.raw/.bin track image to .dat),
.raw --> .mpg, .cif --> .mpg, .mpg --> .mpg, .mpg --> .dat,
.dat --> .mpg.

%description -l pl.UTF-8
Program pozwala na konwersję plików MPEG w różnych formatach:
.cue --> .raw (.cue do obrazu ścieżki .raw/.bin), .cue --> .dat,
.cue --> .mpg, .raw --> .dat (obraz ścieżki .raw/.bin do .dat),
.raw --> .mpg, .cif --> .mpg, .mpg --> .mpg, .mpg --> .dat,
.dat --> .mpg

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT

install -d			$RPM_BUILD_ROOT%{_bindir}
install %{name}			$RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog Credits
%attr(755,root,root) %{_bindir}/*
