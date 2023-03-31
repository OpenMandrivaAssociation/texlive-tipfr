Name:		texlive-tipfr
Version:	38646
Release:	2
Summary:	Produces calculator's keys with the help of TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tipfr
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tipfr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tipfr.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides commands to draw calculator keys with the
help of TikZ. It also provides commands to draw the content of
screens and of menu items.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tipfr
%doc %{_texmfdistdir}/doc/latex/tipfr

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
