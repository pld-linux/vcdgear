Summary:	Convert various MPEG file format
Summary(pl):	Konwerter ró¿nego rodzaju plików MPEG
Name:		vcdgear
Version:	1.6b
Release:	1
License:	unknown
Group:		Applications/File
Group(de):	Applikationen/Datei
Group(pl):	Aplikacje/Pliki
Source:		http://www.vcdgear.com/files/%{name}16b_i386_redhat62.tar.gz
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

%description -l pl
Program pozwala na konwersjê plików MPEG w ró¿nych formatach:
.cue --> .raw (.cue do obrazu ¶cie¿ki .raw/.bin), .cue --> .dat,
.cue --> .mpg, .raw --> .dat (obraz ¶cie¿ki .raw/.bin do .dat),
.raw --> .mpg, .cif --> .mpg, .mpg --> .mpg, .mpg --> .dat,
.dat --> .mpg

%prep
%setup -q -n %{name}16

%install
rm -rf $RPM_BUILD_ROOT

install -d			$RPM_BUILD_ROOT%{_bindir}
install %{name}[0-9][0-9]	$RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/*
