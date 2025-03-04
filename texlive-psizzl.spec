Name:		texlive-psizzl
Version:	69742
Release:	1
Summary:	A TeX format for physics papers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/psizzl
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psizzl.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psizzl.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psizzl.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
PSIZZL is a TeX format for physics papers written at SLAC and
used at several other places. It dates from rather early in the
development of TeX82; as a result, some of the descriptions of
limitations look rather quaint to modern eyes.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/psizzl/base/chapters.Psizzl
%{_texmfdistdir}/tex/psizzl/base/citation.Psizzl
%{_texmfdistdir}/tex/psizzl/base/fontdefs.Psizzl
%{_texmfdistdir}/tex/psizzl/base/index.Psizzl
%{_texmfdistdir}/tex/psizzl/base/institut.Psizzl
%{_texmfdistdir}/tex/psizzl/base/letter.Psizzl
%{_texmfdistdir}/tex/psizzl/base/lists.Psizzl
%{_texmfdistdir}/tex/psizzl/base/macros.Psizzl
%{_texmfdistdir}/tex/psizzl/base/memo.Psizzl
%{_texmfdistdir}/tex/psizzl/base/mypsizzl.tex
%{_texmfdistdir}/tex/psizzl/base/options.Psizzl
%{_texmfdistdir}/tex/psizzl/base/output.Psizzl
%{_texmfdistdir}/tex/psizzl/base/picture.Psizzl
%{_texmfdistdir}/tex/psizzl/base/psizzl.tex
%{_texmfdistdir}/tex/psizzl/base/publicat.Psizzl
%{_texmfdistdir}/tex/psizzl/base/symbols.Psizzl
%{_texmfdistdir}/tex/psizzl/base/thesis.Psizzl
%{_texmfdistdir}/tex/psizzl/config/psizzl.ini
%doc %{_texmfdistdir}/doc/otherformats/psizzl/base/psizzl.commands
%doc %{_texmfdistdir}/doc/otherformats/psizzl/base/psizzl.doc
#- source
%doc %{_texmfdistdir}/source/psizzl/base/aaaread.me

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
