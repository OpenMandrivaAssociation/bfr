%define name	bfr
%define version	1.6
%define release 8

Name: 	 	%{name}
Summary: 	General-purpose command-line pipe buffer
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		https://www.glines.org:8000/software/buffer.html
License:	GPL
Group:		System/Kernel and hardware
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Buffer is a general-purpose command-line pipe buffer. It buffers data from
stdin and sends it to stdout, adjusting to best fit the pace stdout can
handle. It can solve problems on either end of a pipe. For instance, if the
incoming stream is slower than outgoing, performance is mainly dependent on
the "start-stream threshold" you set. This can be used to group data into
larger packets to, for an example, reduce seeking on a tape drive. In the
case of the outgoing being slower, the "stop-stream threshold" prevents
unnecessary CPU from being taken up by reading single-bytes and such (if the
output stream accepts data one byte at a time, for instance), and will
output-only until the buffer goes down to 97% or so. This speeds up certain
procedures, such as creating a tar file, gzipping it, and putting it through
a program such as "netcat". It boosts performance by allowing a certain level
of detachment between the two... allowing tar and (especially) gzip to do its
work at the same time the network is doing its work, so you're not sending
one packet and THEN seeing gzip kick in to create the next.

The Buffer distribution also contains a variant of buffer named Bufplay (bfp).
Bufplay's purpose is to do the same sort of buffering as Buffer, but it is
intended for use with OSS, configuring /dev/dsp for the type of sound data
you specify and playing it. If, for some reason, you want to be cool like me
and have 60 megs of RAM inbetween mpg123 and your sound card, you can. =)

%prep
%setup -q

%build
%configure
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{_bindir}/bfr
%{_bindir}/bfp
%{_mandir}/man1/bfr.1.*




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.6-7mdv2011.0
+ Revision: 616747
- the mass rebuild of 2010.0 packages

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 1.6-6mdv2010.0
+ Revision: 424032
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.6-5mdv2009.0
+ Revision: 243212
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.6-3mdv2008.1
+ Revision: 135828
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Feb 08 2007 Stefan van der Eijk <stefan@mandriva.org> 1.6-3mdv2007.0
+ Revision: 118197
- rebuild
- Import bfr

* Tue Nov 08 2005 Austin Acton <austin@mandriva.org> 1.6-2mdk
- Rebuild

* Sat Apr 03 2004 Austin Acton <austin@mandrake.org> 1.6-1mdk
- 1.6

